import email
from pydantic import BaseModel


## Request schemas


class RegisterRequest(BaseModel):
    """
    Pydantic request model schema used by `/api/register` endpoint
    """

    email: str
    first_name: str
    last_name: str
    username: str


class InitRequest(BaseModel):
    """
    Pydantic request model schema used by `/api/init` endpoint
    """

    username: str
    assessment_name: str
    latest_commit: str


class CheckRequest(BaseModel):
    """
    Pydantic request model schema used by `/api/check` endpoint
    """

    latest_commit: str
    passed: bool


class ApproveRequest(BaseModel):
    """
    Pydantic request model schema used by `/api/approve` endpoint
    """

    latest_commit: str
    reviewer_username: str


class ViewRequest(BaseModel):
    """
    Pydantic request model schema used by `/api/view` endpoint
    """

    username: str
    assessment_name: str


class DeleteRequest(BaseModel):
    """
    Pydantic request model schema used by `/api/delete` endpoint
    """

    username: str
    assessment_name: str


class UpdateRequest(BaseModel):
    """
    Pydantic request model schema used by the `/api/update` endpoint
    """

    username: str
    assessment_name: str
    latest_commit: str
    log: dict


class ReviewRequest(BaseModel):
    """
    Pydantic request model schema used by `/api/review` endpoint
    """

    latest_commit: str


## Response schemas


class RegisterResponse(BaseModel):
    """
    Pydantic response model schema used by `/api/register` endpoint
    """

    registered: bool


class InitResponse(BaseModel):
    """
    Pydantic response model schema used by `/api/init` endpoint
    """

    Initiated: bool
    User_first_name: str


class ReviewResponse(BaseModel):
    """
    Pydantic response model schema used by `/api/review` endpoint
    """

    id: int
    reviewer_username: str
