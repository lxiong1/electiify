class IdConstants:
    ID = "id"


class BaseTextConstants:
    TEXT = "text"


class QuestionConstants(BaseTextConstants, IdConstants):
    QUESTION_ID = "question_id"


class AnswerConstants(QuestionConstants):
    ANSWER_ID = "answer_id"
    QUESTION = "question"


class ChoiceConstants(QuestionConstants):
    QUESTION = "question"
    VOTES = "votes"
