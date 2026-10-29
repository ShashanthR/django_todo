from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskViewTests(TestCase):
    def test_add_task_creates_pending_task(self):
        response = self.client.post(reverse('addTask'), {'task': 'Write tests'})

        self.assertRedirects(response, reverse('home'))
        task = Task.objects.get(task='Write tests')
        self.assertFalse(task.is_completed)

    def test_undo_completed_task_returns_it_to_pending_list(self):
        task = Task.objects.create(task='Completed task', is_completed=True)

        response = self.client.post(reverse('undoTask', args=[task.pk]))

        self.assertRedirects(response, reverse('home'))
        task.refresh_from_db()
        self.assertFalse(task.is_completed)

        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Completed task')

    def test_edit_complete_and_delete_task(self):
        task = Task.objects.create(task='Original task')

        response = self.client.post(
            reverse('editTask', args=[task.pk]),
            {'task': 'Updated task'},
        )
        self.assertRedirects(response, reverse('home'))
        task.refresh_from_db()
        self.assertEqual(task.task, 'Updated task')

        response = self.client.post(reverse('mark_as_done', args=[task.pk]))
        self.assertRedirects(response, reverse('home'))
        task.refresh_from_db()
        self.assertTrue(task.is_completed)

        response = self.client.post(reverse('deleteTask', args=[task.pk]))
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
