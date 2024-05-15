# jpydzr5-car-share-info
# init
## Pomocne linki
Link: [jira board](https://jira.is-academy.pl/secure/RapidBoard.jspa?projectKey=JPYDZR5CSI&useStoredSettings=true&rapidView=735)\
Link: [github repo](https://github.com/infoshareacademy/jpydzr5-car-share-info)\
Link: [cookiecutter](https://github.com/cookiecutter/cookiecutter-django)

## To-do
1. Zapoznać się z naszym jira boardem
2. Sklonować repozytorium
3. Stworzyć swojego brancha(nazwą może być nick)\
Swój branch niech będzie zrobiony na podstawie brancha development
4. Poczytać o cookiecutter django jeżeli chcemy więcej wiedzieć o templacie, który został stworzony
5. Przyswoić sobie formatowanie kodu za pomocą formatera Black
6. Poczytać o pydantic, ponieważ postaramy się go używać (wiem, jest to trudne)\
Zdaje się, że pydantic to @dataclass z dodatkowymi opcjami

## Zasady mergowania
- przed mergowaniem upewniamy się, że nasze repozytorium jest aktualne, żeby nie powstawały konflikty
- mergujemy ze swojego brancha do development branch czyli:
- jeżeli uznamy, że branch development spełnia wymagania projektu to zmergujemy go do main branch
1. `git checkout development`
2. `git fetch/git pull` dla upewnienia się, że nasz development branch jest up-to-date
3. `git merge <nazwa-własnego brancha>`
4. `git push` żeby merg był dostępny dla wszystkich
- możemy też pomyśleć o tworzeniu branchów w inny sposób\
tj. tak jak mówił Piotr na zajęciach z gita, że możemy tworzyć\
np. feature1, feature2

## Spotkania
- być może dobrze będzie jeżeli z wyprzedzeniem ustalimy kiedy będziemy się spotykać na krótkie briefingi.
