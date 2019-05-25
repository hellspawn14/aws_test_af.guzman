import json
import unittest
import requests 
import hashlib
import time
import random

class obtener_historial_campanias_test(unittest.TestCase):
    
    def registrar_usuario(self, user_name, user_email, user_password):
        service_end_point = 'http://localhost:5000/registrar_usuario'
        data = dict(user_name = user_name, user_email = user_email, user_password = user_password)
        headers = {'Content-type': 'application/json'}
        response = requests.post(url = service_end_point, data = json.dumps(data), headers = headers)
        return response

    def iniciar_sesion(self, user_email, user_password):
        service_end_point = 'http://localhost:5000/iniciar_sesion'
        user_password_sha256 = hashlib.sha256(user_password.encode()).hexdigest()
        data = dict(user_email = user_email, user_password = user_password_sha256)
        headers = {'Content-type': 'application/json'}
        response = requests.post(url = service_end_point, data = json.dumps(data), headers = headers)
        return response

    def create_new_campaign(self, user_email, subject, number_of_recipients):
        service_end_point = 'http://localhost:5000/create_new_campaign'
        data = dict(user_email = user_email, subject = subject, number_of_recipients = number_of_recipients)
        headers = {'Content-type': 'application/json'}
        response = requests.post(url = service_end_point, data = json.dumps(data), headers = headers)
        return response

    def delete_campaign(self, id_campaign):
        service_end_point = 'http://localhost:5000/delete_campaign'
        data = dict(id_campaign = id_campaign)
        headers = {'Content-type': 'application/json'}
        response = requests.post(url = service_end_point, data = json.dumps(data), headers = headers)
        return response 

    def obtener_historial(self, user_email):
        service_end_point = 'http://localhost:5000/obtener_historial'
        data = dict(user_email = user_email)
        headers = {'Content-type': 'application/json'}
        response = requests.post(url = service_end_point, data = json.dumps(data), headers = headers)
        return response 
    
    # Crear 5 campanias y obtener archivo 
    def test_1(self):
        user_name = 'john doe'
        user_email = 'j.doe@email.com'
        user_password = 'ABCD' 
        # Registrar usuario para test
        self.registrar_usuario(user_name, user_email, user_password)
        
        for i in range(5):
            subject = 'campain ' + str(i)
            number_of_recipients = random.randint(1, 100)
            self.create_new_campaign(user_email, subject, number_of_recipients)
            time.sleep(5) 
        
        response = self.obtener_historial(user_email)
        message = json.loads(response.text)
        self.assertEqual('XXXX', message)

   
if __name__ == "__main__":
    unittest.main()
