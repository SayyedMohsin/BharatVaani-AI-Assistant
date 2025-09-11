{
  "name": "UserProfile",
  "type": "object",
  "properties": {
    "preferred_language": {
      "type": "string",
      "enum": [
        "hindi",
        "english",
        "tamil",
        "telugu",
        "bengali",
        "marathi",
        "gujarati",
        "punjabi",
        "kannada",
        "malayalam"
      ],
      "default": "hindi",
      "description": "User's preferred language"
    },
    "location": {
      "type": "string",
      "description": "User's location for local services"
    },
    "phone_number": {
      "type": "string",
      "description": "User's phone number"
    },
    "upi_id": {
      "type": "string",
      "description": "User's UPI ID"
    },
    "voice_enabled": {
      "type": "boolean",
      "default": true,
      "description": "Whether voice commands are enabled"
    }
  },
  "required": []
}