from client import ShamirSecretSharing

def main():
    print("=== Testing Shamir Secret Sharing ===")
    sss = ShamirSecretSharing(prime=10007)
    secret = 2024
    
    shares = sss.split_secret(secret, k=3, n=5)
    print(f"Secret: {secret}")
    print(f"Generated 5 Shares: {shares}")
    
    # Reconstruct from shares 0, 1, 2
    rec = sss.reconstruct_secret(shares[:3])
    print(f"Reconstructed from first 3 shares: {rec}")
    assert rec == secret
    
    # Reconstruct from arbitrary 3 shares
    rec_alt = sss.reconstruct_secret([shares[0], shares[2], shares[4]])
    print(f"Reconstructed from shares [0, 2, 4]: {rec_alt}")
    assert rec_alt == secret
    print("=== Shamir Secret Sharing Verification Complete ===")

if __name__ == "__main__":
    main()
