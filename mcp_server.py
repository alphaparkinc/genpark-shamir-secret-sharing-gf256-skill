from client import ShamirSecretSharing
import json

def handle_request(req):
    sss = ShamirSecretSharing()
    action = req.get("action")
    if action == "split":
        sec = req.get("secret", 0)
        k = req.get("k", 3)
        n = req.get("n", 5)
        shares = sss.split_secret(sec, k, n)
        return {"status": "ok", "shares": shares}
    elif action == "reconstruct":
        shares = [tuple(s) for s in req.get("shares", [])]
        rec = sss.reconstruct_secret(shares)
        return {"status": "ok", "secret": rec}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "split", "secret": 1234})))
