def article_validate(article):
    errors = {}
    if not article.title:
        errors["title"] = "Название обязательное поле"
    elif len(article.title) > 3:
        errors["title"] = "Длина название не может быть больше чем 50 символов"
    if not article.content:
        errors["content"] = "Контент обязательное поле"
    elif len("content") > 1000:
        errors["content"] = "Длина контента не может быть больше чем 1000 символов"
    if not article.author:
        errors["author"] = "Автор обязательное поле"
    elif len(article.author) > 50:
        errors["author"] = "Длина имени автора не может быть больше чем 50 символов"

    return errors