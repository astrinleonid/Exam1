class Review:
    def __init__(self, review_id, txt, positives, negatives):
        """
        Initialize a movie review.  Checks positive, negative and unknown words in the review,
            decides if it's positive
        :param review_id: id of the review
        :param txt: text of the review
        :param positives: words that are considered positive
        :param negatives: words that are considered negative
        """
        ...  # Replace with your code here

        self.id = review_id
        self.txt = txt
        self.words_pos = []
        self.words_neg = []
        self.words_unknown = []
        words_all = self.__parse_text__(txt)
        for i, word in enumerate(words_all):
            if word in positives:
                self.words_pos.append(word)
            elif word in negatives:
                self.words_neg.append(word)
            else:
                self.words_unknown.append(word)
        self.positive = (len(self.words_pos) > len(self.words_neg))

        self.score = (len(self.words_pos) - len(self.words_neg))/len(words_all)

    def __parse_text__(self, text):
        """
        Returns the list of words appeared in the text
        """
        raw_list = text.split()
        words = []
        for word in raw_list:
           words.append((word.strip(' ').lower()))

        return words


class MovieReviews:


    def __init__(self, reviews_file, words_file):

        """
           Initialize Movie Reviews engine by parsing the reviews
               and file with words categorized by positive / negative sentiment
           :param reviews_file: file of movie reviews (each review on a new line)
           :param words_file: file with pairs of words and sentiment ('pos' for positive, 'neg' for negative)
        """

        (self.__neg__,self.__pos__) = self.parse_words_file(words_file)
        review_lines = self.parse_reviews_file(reviews_file)
        self.__reviews__ = [Review(i, line, self.__pos__, self.__neg__) for i, line in enumerate(review_lines)]


    def parse_words_file(self, words_file):
        """
        Opens a file with tagged words and returns a tuple of two lists, negative and positive
        """

        flie = open(words_file, "r")

        pos = []
        neg = []

        for line in flie:
            [word, tag] = line.split()
            if tag == "pos":
                pos.append(word)
            if tag == "neg":
                neg.append(word)
        return (neg, pos)
        file.close()

    def parse_reviews_file(self, filename):
        """
        Opens a file with reviews and returns a list of lines
        """

        flie = open(filename, "r")
        reviews = []
        for line in flie:
           reviews.append(line.strip(' \n'))
        return reviews
        file.close()

    def get_reviews_by_score(self):
        """
        Returns the list of reviews sorted by their score
        """

        scored_reviews = []
        for review in self.__reviews__:
            scored_reviews.append((review.score, review))
        review_list_sorted = sorted(scored_reviews, key=lambda scored_reviews: scored_reviews[0], reverse=True)

        return [review for (score, review) in review_list_sorted]

    def __getitem__(self, item):

        return self.__reviews__[item]


##############################################################################
# WARNING: test code follows, do not change!
##############################################################################


def regular_test():
    reviews = MovieReviews(reviews_file='reviews.txt',
                           words_file='words.txt')
    print('\n=== TEST: 1st review:')
    # Print important information about the 1st review
    #   Hint1: what method needs to be added to access element 0 of reviews?
    #   Hint2: what method needs to be added to print?
    print(reviews[0])
    assert reviews[0].id == 0
    assert len(reviews[0].txt) == 102
    assert reviews[0].words_pos == []
    assert reviews[0].words_neg == ['depressing', 'bad']
    assert reviews[0].words_unknown == ['"a', 'rating', 'of', '""1""', 'does', 'not', 'begin', 'to', 'express', 'how',
                                        'dull,', 'and', 'relentlessly', 'this', 'movie', 'is."']
    assert not reviews[0].positive

    # Verify all reviews sentiment result (positive / negative) is correct
    print('\nTEST: Are reviews positive:', [review.positive for review in reviews])
    for review, positive in zip(reviews, [False, False, True, True, True, True, False]):
        assert review.positive == positive

    print('\nTEST: Regular test passed!\n')
    return reviews


def bonus_test(reviews):
    print('\nTEST: Start BONUS test')
    reviews_by_score = reviews.get_reviews_by_score()
    print('TEST: Ids of reviews sorted by score:', [round(review.id, 2) for review in reviews_by_score])
    print('TEST: Scores of reviews sorted by score:', [round(review.score, 3) for review in reviews_by_score])
    # Check that positive reviews appear first
    for review, positive in zip(reviews_by_score, [True, True, True, True, False, False, False]):
        assert review.positive == positive
    # Check correct order of reviews from positive to negative
    for review, positive in zip(reviews_by_score, [5, 3, 2, 4, 0, 6, 1]):
        assert review.id == positive
    print('\nTEST: Best review:')
    print(reviews_by_score[0])
    print('\nTEST: Worst review:')
    print(reviews_by_score[-1])
    print('\nTEST: BONUS test passed!')


if __name__ == '__main__':
    reviews_ = regular_test()
    bonus_test(reviews_)