Задание:
• Создайте веб-приложение , с API интерфейсом и админ-панелью.
• Создайте базу данных используя миграции Django
Требования:
1. Информация о каждом сотруднике должна храниться в базе данных и содержать
следующие данные:
• ФИО;
• Должность;
• Дата приема на работу;
• Размер заработной платы;
• Информация о выплаченной зарплате;
2. У каждого сотрудника есть 1 начальник;
3. База данных должна содержать 5 уровней иерархий;
4. На странице сотрудников в админ-панели должны выводиться:
• ФИО.
• Должность.
• Ссылка на объект начальника.
• Заработная плата.
• Всего выплачено.
5. На странице сотрудников в админ-панели должны быть фильтры:
• Должность.
• Уровень.
6. На странице сотрудников в админ-панели должен быть action который удаляет всю
информацию о выплаченной заработной плате всех выбранных сотрудников.
7. Используя DRF, создать набор представлений:
• Все данные о сотрудниках.
• Все данные о сотрудниках одного уровня.
8. Сотрудники с определенной группой прав должны иметь доступ к API;
