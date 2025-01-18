class SignatureValidator:
    def validate(self, signature):
        # Simulate signature validation logic
        if not signature or len(signature) < 10:  # Example logic
            raise ValueError("Invalid signature")
        return True
