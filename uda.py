"""Count words."""
from collections import Counter
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    str=s.split()
    # TODO: Count the number of occurences of each word in s
    list1=Counter(str).most_common()
    str1=sorted(list1,key=lambda list1:(-list1[1],list1[0]),reverse=False)
    # TODO: Return the top n most frequent words.
    return  str1[:n]


def test_run():
    """Test count_words() with some inputs."""
    print (count_words("cat bat mat cat bat cat", 3))
    print (count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()
