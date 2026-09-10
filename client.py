class ShamirSecretSharing:
    """
    Shamir's (k, n) Threshold Secret Sharing Scheme.
    Splits a secret into n shares such that any k shares can reconstruct it via Lagrange interpolation.
    """
    def __init__(self, prime=10007):
        self.prime = prime

    def split_secret(self, secret, k, n):
        coeffs = [secret] + [(secret * 3 + i * 7) % self.prime for i in range(1, k)]
        shares = []
        for x in range(1, n + 1):
            y = 0
            for power, c in enumerate(coeffs):
                y = (y + c * pow(x, power, self.prime)) % self.prime
            shares.append((x, y))
        return shares

    def reconstruct_secret(self, shares):
        secret = 0
        k = len(shares)
        for i in range(k):
            xi, yi = shares[i]
            li = 1
            for j in range(k):
                if i != j:
                    xj, _ = shares[j]
                    num = (-xj) % self.prime
                    den = pow((xi - xj) % self.prime, self.prime - 2, self.prime)
                    li = (li * num * den) % self.prime
            secret = (secret + yi * li) % self.prime
        return secret
