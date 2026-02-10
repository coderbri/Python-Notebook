##############################################################
# File:           facebook_likes_counter.py
# Description:    Handling missing dictionary keys in a loop.
#                 Uses try-except to prevent a KeyError when
#                 summing values from inconsistent data structures.
##############################################################

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},   # ! Missing 'Likes'
    {'Comments': 1, 'Shares': 1},   # ! Missing 'Likes'
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            # ? If the 'Likes' key is missing, skip it by adding 0
            pass

    return total_likes

print(count_likes(facebook_posts))  # Output: 86