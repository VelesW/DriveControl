from ..repositories.rental_repository import RentalRepository
from ..utils.signature_validator import SignatureValidator


class RentalService:
    def __init__(self, rental_repository: RentalRepository, signature_validator: SignatureValidator):
        self.rental_repository = rental_repository
        self.signature_validator = signature_validator

    def handle_form_submission(self, form_data):
        # Validate the signature
        if not self.signature_validator.validate(form_data.get("signature", "")):
            raise ValueError("Invalid signature")

        # Save the form
        return self.rental_repository.save_form(form_data)
