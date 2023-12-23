import flet as ft
from fletrt import RouteView

from sklearn.ensemble import RandomForestClassifier

import pickle


class Index(RouteView):
    def __init__(self):
        super().__init__()

        self.smoking_history_options_map = {
            'never': 0,
            'current': 2,
            'former': 3,
            'ever': 4,
            'not current': 5
        }

        self.smoking_history_options = [
            ft.dropdown.Option(option) for option in self.smoking_history_options_map.keys()
        ]

        self.gender_options = [
            ft.dropdown.Option('Female'),
            ft.dropdown.Option('Male'),
        ]

        self.model: RandomForestClassifier = pickle.load(open('./objects/model.pkl', 'rb'))

    def calculate(self, gender, age, hyper, heart, smoking, bmi, hba1c, glucose):
        smoking_value = 0

        if smoking != 'none':
            smoking_value = self.smoking_history_options_map[smoking]

        predict_target = [
            0 if gender == 'Female' else 1,
            age,
            1 if hyper else 0,
            1 if heart else 0,
            smoking_value,
            bmi,
            hba1c,
            glucose
        ]

        result = self.model.predict([predict_target])[0]

        dlg = ft.AlertDialog(
            title=ft.Text(f"Result"),
            content=ft.Text(f"The predicted result is: {'Positive' if result == 1 else 'Negative'}")
        )

        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def body(self):
        title = ft.Text('Diabetes Classificator', size=50, text_align=ft.TextAlign.CENTER)
        age = ft.TextField(label="Age")
        gender = ft.Dropdown(label="Gender", options=self.gender_options)
        hyper = ft.Checkbox(label="Hypertension")
        heart = ft.Checkbox(label="Heart disease")
        smoking = ft.Dropdown(label="Smoking history", options=self.smoking_history_options)
        bmi = ft.TextField(label="BMI")
        hba1c = ft.TextField(label="HbA1c level")
        glucose = ft.TextField(label="Blood glucose level")
        confirm = ft.ElevatedButton('Calculate')

        smoking.value = 'none'

        title.width = self._page.width

        confirm.width = self._page.width
        confirm.height = 50
        confirm.on_click = lambda _: self.calculate(gender.value, age.value, hyper.value, heart.value, smoking.value,
                                                    bmi.value,
                                                    hba1c.value, glucose.value)

        return ft.Container(
            margin=ft.margin.symmetric(8, 32),
            content=ft.Column(
                controls=[
                    ft.Container(
                        margin=ft.margin.symmetric(32, 0),
                        content=title
                    ),
                    gender,
                    age,
                    hyper,
                    heart,
                    smoking,
                    bmi,
                    hba1c,
                    glucose,
                    ft.Container(
                        margin=ft.margin.only(0, 16, 0, 0),
                        content=confirm
                    )
                ]
            )
        )
