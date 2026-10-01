from YG_Projects import YGProject

key = "ВСТАВЬ ТОКЕН СЮДА"
api = YGProject("https://ru.yougile.com/api-v2", key)


# Позитивный тест: создание нового проекта
def test_create_project():
    new_project = api.create_project("Автоматизация")

    assert new_project.status_code == 201


# Негативный тест: создание проекта с пустым именем
def test_create_noname_project():
    new_project = api.create_project("")

    assert new_project.status_code == 400


# Позитивный тест: изменение имени проекта
def test_change_name():
    new_project = api.create_project("Автоматизация")
    resp = new_project.json()
    project_id = resp["id"]

    new_name = "Automatization"
    project = api.change_name_project(project_id, new_name)
    body = project.json()
    assert project.status_code == 200
    assert body["id"] == project_id


# Негативный тест: изменение имени проекта с несуществующим id
def test_change_name_invalid_id():
    invalid_id = "0000000000"
    new_name = 'Auto'
    resp = api.change_name_project(invalid_id, new_name)

    assert resp.status_code == 404


# Позитивный тест: удаление проекта
def test_delete_project():
    new_project = api.create_project("Автоматизация")
    resp = new_project.json()
    project_id = resp["id"]

    project = api.delete_project(project_id)
    assert project.status_code == 200


# Негативный тест: удаление проекта с несуществующим id
def test_delete_name_invalid_id():
    invalid_id = "0000000000"
    resp = api.delete_project(invalid_id)

    assert resp.status_code == 404


# Позитивный тест: получение проекта по id
def test_get_project_with_id():
    new_project = api.create_project("Автоматизация")
    resp = new_project.json()
    project_id = resp["id"]

    project = api.get_project_with_id(project_id)
    body = project.json()
    assert project.status_code == 200
    assert body["id"] == project_id


# Негативный тест: получение проекта по несуществующему id
def test_get_project_with_invalid_id():
    invalid_id = "1234567890"
    project = api.get_project_with_id(invalid_id)

    assert project.status_code == 404
