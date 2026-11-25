from app import app    
def test_health():     
    client = app.test_client()     
    reponse = client.get("/health")    
    assert reponse.status_code == 200     
    assert reponse.get_json()["status"] == "ok"    


def test_get_colis_existant():
    client = app.test_client()
    response = client.get("/colis/GT-1001")
    assert response.status_code == 200
    assert response.get_json()["client"] == "SOTELGAB"

def test_get_colis_inconnu():
    client = app.test_client()
    response = client.get("/colis/GT-9999")
    assert response.status_code == 404
    assert response.get_json()["colis"] == "Colis  introuvable"