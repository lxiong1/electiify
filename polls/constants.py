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
    CHOICE_ID = "choice_id"
    QUESTION = "question"
    VOTES = "votes"
