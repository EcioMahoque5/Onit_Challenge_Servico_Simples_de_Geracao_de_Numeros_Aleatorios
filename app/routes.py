from flask import Blueprint, request, make_response
import logging
from .validators import RandomNumberForm
import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

api_bp = Blueprint('api', __name__)


@api_bp.route('/generate_random_number', methods=['POST'])
def generate_random_number():
    data = request.get_json()
    form = RandomNumberForm(data=data)
    
    logger.info(f"generate_random_number request received: {data}")
    try:
        if form.validate():
            min_value = int(data.get('min'))
            max_value = int(data.get('max'))
            
            random_number = random.randint(min_value, max_value)
            
            logger.info("generate_random_number response {}".format(
                {
                    "min": min_value,
                    "max": max_value,
                    "random_number": random_number
                }
            ))
            
            return make_response({
                "success": True,
                "min": min_value,
                "max": max_value,
                "random_number": random_number
            }, 200)
            
        else:
            logger.error({
                "message": "Validations errors",
                "errors": form.errors,
            })
            return make_response({
                "success": False,
                "message": "Validations errors",
                "errors": form.errors
            }, 409)
    
    except Exception as e:
        logger.error(e, exc_info=True)
        logger.info(f"error {e} occured on generate_random_number api")
        return make_response({
            "message": "An unexpected error occurred. Please try again later!",
            "code": 500
        }, 500)
