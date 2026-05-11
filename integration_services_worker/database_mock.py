from typing import List, Optional
import utils

class Car:
    def __init__(self, vin: str, model_id: str, brand: str, model_name: str, year: int, color: str, car_body_type: str, price: float, image: Optional[str] = None):
        self.vin = vin
        self.model_id = model_id
        self.brand = brand
        self.model_name = model_name
        self.year = year
        self.color = color
        self.car_body_type = car_body_type
        self.price = price
        self.image = utils.image_to_base64_compressed(image) if image else None
     
    def to_dict(self):
        return self.__dict__

class DatabaseMock:
    def __init__(self):
        self.cars: List[Car] = [
            Car(
                vin="1HGCM82633A123456",
                model_id="Toyota_Corolla",
                brand="Toyota",
                model_name="Corolla",
                year=2020,
                color="white",
                car_body_type="sedan",
                price=75000,
                image=r"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Toyota_Corolla_Limousine_Hybrid_Genf_2019_1Y7A5576.jpg/960px-Toyota_Corolla_Limousine_Hybrid_Genf_2019_1Y7A5576.jpg"
            ),
            Car(
                vin="JTMRFREV0ED123456",
                model_id="Toyota_RAV4",
                brand="Toyota",
                model_name="RAV4",
                year=2022,
                color="grey",
                car_body_type="suv",
                price=135000,
                image=r"https://cdn-ab.spidersweb.pl/2019/05/Toyota-RAV4-2019-hybrid-test-30.webp"
            ),
            Car(
                vin="WBAJA9C50JB123456",
                model_id="BMW_X3",
                brand="BMW",
                model_name="X3",
                year=2023,
                color="blue",
                car_body_type="suv",
                price=210000,
                image=r"https://cms-assets.autoscout24.com/uaddx06iwzdz/765HMsN4QTlCLGta4LZrhI/5876ffc99061e95d9b2bcc6138add796/bmw-x3-l-01.jpg?w=1100"
            ),
            Car(
                vin="WAUZZZ8V5KA123456",
                model_id="Audi_A4",
                brand="Audi",
                model_name="A4",
                year=2021,
                color="white",
                car_body_type="sedan",
                price=160000,
                image=r"https://autospot.com.pl/panel/uploads_uzywane/780/Audi%20A4%2003.12.24%20profilowe.jpg"
            ),
            Car(
                vin="WDD2051231F123456",
                model_id="Mercedes_C-Class",
                brand="Mercedes",
                model_name="C-Class",
                year=2021,
                color="silver",
                car_body_type="sedan",
                price=180000,
                image=r"https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0326/47718ef0a7bb4c0a9a9d0b8259914fae_ful.jpg"
            ),
            Car(
                vin="WVWZZZ1KZPW123456",
                model_id="Volkswagen_Golf",
                brand="Volkswagen",
                model_name="Golf",
                year=2019,
                color="red",
                car_body_type="hatchback",
                price=68000,
                image=r"https://autocentrumgroup.pl/wp-content/uploads/2024/08/2020_Volkswagen_Golf_Style_1.5_Front-scaled.jpg"
            )
        ]

    def get_car_by_vin(self, vin: str) -> Optional[Car]:
        return next((car for car in self.cars if car.vin == vin), None)
    
    def get_car_by_model_id(self, model_id: str) -> Optional[Car]:
        return next((car for car in self.cars if car.model_id == model_id), None)