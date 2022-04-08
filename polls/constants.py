class IdConstants:
    ID = "id"


class BaseTextConstants:
    TEXT = "text"


class QuestionConstants(BaseTextConstants, IdConstants):
    pass


class AnswerConstants(BaseTextConstants, IdConstants):
    QUESTION_ID = "question_id"
    QUESTION = "question"


class MultiChoiceAnswerConstants(BaseTextConstants, IdConstants):
    QUESTION_ID = "question_id"
    QUESTION = "question"
    VOTES = "votes"
