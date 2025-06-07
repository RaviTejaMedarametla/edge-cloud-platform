from fastapi.testclient import TestClient
import importlib.util
import sys
import types
from pathlib import Path

service_dir = Path(__file__).resolve().parents[1]
package_name = "order_service"
package = types.ModuleType(package_name)
package.__path__ = [str(service_dir)]
sys.modules[package_name] = package

spec = importlib.util.spec_from_file_location(
    f"{package_name}.main", service_dir / "main.py"
)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
app = module.app

client = TestClient(app)

def test_create_and_get_order():
    order_data = {"id": 1, "item": "Book", "quantity": 2, "price": 9.99, "status": "pending"}
    resp = client.post("/orders", json=order_data)
    assert resp.status_code == 200
    assert resp.json() == order_data

    resp = client.get("/orders/1")
    assert resp.status_code == 200
    assert resp.json() == order_data

    resp = client.get("/orders")
    assert resp.status_code == 200
    assert len(resp.json()) == 1
