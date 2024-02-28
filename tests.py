import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_three_book(self):
        collector = BooksCollector()
        collector.add_new_book('Студёное дыхание')
        collector.add_new_book('Сто лет тому вперёд')
        collector.add_new_book('Война и мир')

        assert len(collector.get_books_genre()) == 3

    @pytest.mark.parametrize('name',
                             [
                                 'Робинзона Крузо. Жизнь, необыкновенные и удивительные приключения Робинзона Крузо, моряка из Йорка, прожившего двадцать восемь лет в полном одиночестве на необитаемом острове у берегов Америки близ устьев реки Ориноко, куда он был выброшен кораблекрушением, во время которого весь экипаж корабля, кроме него, погиб, с изложением его неожиданного освобождения пиратами; написанные им самим',
                                 ''
                             ]
                             )
    def test_add_new_book_add_book_with_long_and_empty_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_one_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Зелёная миля')
        collector.set_book_genre('Зелёная миля', 'Фантастика')

        assert collector.get_book_genre('Зелёная миля') == 'Фантастика'

    def test_set_book_genre_add_one_different_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Стив Джобс и я: подлинная история Apple')
        collector.set_book_genre('Стив Джобс и я: подлинная история Apple', 'Биография')

        assert 'Биография' not in collector.get_books_genre()

    def test_get_books_with_specific_genre_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.add_new_book('Зелёная миля')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.set_book_genre('Зелёная миля', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Ведьмак', 'Зелёная миля']

    def test_get_books_with_specific_genre_get_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.add_new_book('Зелёная миля')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.set_book_genre('Зелёная миля', 'Фантастика')

        assert collector.get_books_with_specific_genre('Комедии') == []
    @pytest.mark.parametrize('name,genre',
                             [
                                 ['Братство кольца', 'Фантастика'],
                                 ['Хочу съесть твою поджелудочную', 'Мультфильмы']
                             ]
                             )
    def test_get_books_for_children_add_two_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name in collector.get_books_for_children()

    @pytest.mark.parametrize('name,genre',
                             [
                                 ['Оно', 'Ужасы'],
                                 ['Шерлок Холмс', 'Детективы']
                             ]
                             )
    def test_get_books_for_children_add_two_books_not_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name not in collector.get_books_for_children()

    def test_get_books_genre_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.add_new_book('Манюня')
        collector.set_book_genre('Манюня', 'Комедии')

        assert collector.get_books_genre() == {'Ведьмак': 'Фантастика', 'Манюня': 'Комедии'}
    @pytest.mark.parametrize('name,genre',
                                [
                                    ['Оно', 'Ужасы'],
                                    ['Шерлок Холмс', 'Детективы']
                                ]
                             )
    def test_set_book_genre_add_two_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Манюня')
        collector.set_book_genre('Манюня', 'Комедии')
        collector.add_book_in_favorites('Манюня')

        assert 'Манюня' in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name,genre',
                             [
                                 ['Оно', 'Ужасы'],
                                 ['Шерлок Холмс', 'Детективы']
                             ]
                             )
    def test_add_book_in_favorites_twice(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_amount_two(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Ведьмак')

        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Комедии')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name,genre',
                             [
                                 ['Оно', 'Ужасы'],
                                 ['Шерлок Холмс', 'Детективы']
                             ]
                             )
    def test_delete_book_from_favorites_twice(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert name not in collector.get_list_of_favorites_books()


    def test_get_list_of_favorites_books_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Ведьмак')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Ведьмак')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Ведьмак']

    def test_get_list_of_favorites_books_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('')
        collector.set_book_genre('', 'Комедии')
        collector.add_book_in_favorites('')

        assert collector.get_list_of_favorites_books() == []
