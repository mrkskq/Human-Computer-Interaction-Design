Креирајте Django апликација за менаџирање на фитнес центар.
Секој тренинг се карактеризира со име на тренингот, инструктор, краток опис, категорија, корисник кој го внел тренингот, слика, цена по тренинг и број на слободни места. За секоја категорија се чува име на категоријата (пр. Кардио, Јога, Сила), опис на категоријата и информација дали е во моментов многу барана (bool). За секој инструктор се чува име, презиме, биографија и ниво на искуство (Почетник, Сертифициран, Професионален тренер).

Сите модели треба да се регистрираат во админ панелот.

При додавање на нов тренинг, полето за корисник не треба да се пополнува рачно, туку системот автоматски да го зачува корисникот кој е во моментот најавен во системот.

<hr>

Create a Django application for managing a fitness center.
Each training session is characterized by the training name, instructor, short description, category, user who added the training, image, price per training session, and number of available spots. For each category, the category name (e.g., Cardio, Yoga, Strength), category description, and information whether it is currently highly demanded (bool) are stored. For each instructor, the first name, last name, biography, and experience level (Beginner, Certified, Professional Trainer) are stored.

All models should be registered in the admin panel.

When adding a new training session, the user field should not be filled manually; instead, the system should automatically save the user who is currently logged into the system.