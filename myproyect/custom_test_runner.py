# custom_test_runner.py

from django.test.runner import DiscoverRunner

class CustomTestRunner(DiscoverRunner):
    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        # Define el orden de ejecución de las aplicaciones
        app_order = ["patient", "allergy"]

        # Filtra las pruebas por aplicación y las ordena según app_order
        filtered_test_labels = []
        for app in app_order:
            filtered_test_labels.extend([label for label in test_labels if label.startswith(f"{app}.")])

        return super().build_suite(filtered_test_labels, extra_tests, **kwargs)
