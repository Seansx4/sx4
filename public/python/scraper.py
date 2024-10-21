# from googlemaps import GoogleMapsScraper
# from datetime import datetime
# import argparse
# import json
# from termcolor import colored
# import os

# ind = {'most_relevant': 0, 'newest': 1, 'highest_rating': 2, 'lowest_rating': 3}
# HEADER = ['id_review', 'caption', 'relative_date', 'retrieval_date', 'rating', 'username', 'n_review_user', 'reviewer_image', 'url_user']
# HEADER_W_SOURCE = ['id_review', 'caption', 'relative_date', 'retrieval_date', 'rating', 'username', 'n_review_user', 'reviewer_image', 'url_user', 'url_source']

# def json_writer(ind_sort_by, path='data/'):
#     outfile = ind_sort_by + '_gm_reviews.json'
#     targetfile_path = path + outfile
#     return targetfile_path

# def serialize_review(review):
#     """Convert review to a serializable format."""
#     return {key: (value.isoformat() if isinstance(value, datetime) else value) for key, value in review.items()}

# def load_existing_reviews(targetfile_path):
#     """Load existing reviews from the JSON file if it exists."""
#     if os.path.exists(targetfile_path):
#         with open(targetfile_path, 'r', encoding='utf-8') as json_file:
#             return json.load(json_file)
#     return []  # Return an empty list if the file does not exist

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Google Maps reviews scraper.')
#     parser.add_argument('--N', type=int, default=100, help='Number of reviews to scrape')
#     parser.add_argument('--i', type=str, default='urls.txt', help='target URLs file')
#     parser.add_argument('--sort_by', type=str, default='newest', help='most_relevant, newest, highest_rating or lowest_rating')
#     parser.add_argument('--place', dest='place', action='store_true', help='Scrape place metadata')
#     parser.add_argument('--debug', dest='debug', action='store_true', help='Run scraper using browser graphical interface')
#     parser.add_argument('--source', dest='source', action='store_true', help='Add source url to JSON file (for multiple urls in a single file)')
#     parser.set_defaults(place=False, debug=False, source=False)

#     args = parser.parse_args()

#     # Prepare to write reviews to JSON file
#     targetfile_path = json_writer(args.sort_by)
    
#     # Load existing reviews to avoid duplicates
#     existing_reviews = load_existing_reviews(targetfile_path)
#     existing_review_ids = {review['id_review'] for review in existing_reviews}  # Track existing review IDs

#     reviews_data = []  # Initialize a list to hold review dictionaries

#     with GoogleMapsScraper(debug=args.debug) as scraper:
#         with open(args.i, 'r') as urls_file:
#             for url in urls_file:
#                 if args.place:
#                     print(scraper.get_account(url))
#                 else:
#                     error = scraper.sort_by(url, ind[args.sort_by])

#                     if error == 0:
#                         n = 0

#                         while n < args.N:
#                             # logging to std out
#                             print(colored('[Review ' + str(n) + ']', 'cyan'))

#                             reviews = scraper.get_reviews(n)
#                             if len(reviews) == 0:
#                                 break

#                             for r in reviews:
#                                 review_id = r['id_review']  # Assuming 'id_review' is the key for the review ID
#                                 if review_id not in existing_review_ids:  # Check against existing IDs
#                                     row_data = serialize_review(dict(r))  # Serialize each review
#                                     if args.source:
#                                         row_data['url_source'] = url.strip()  # Add source URL if needed

#                                     reviews_data.append(row_data)  # Append new review data to the list

#                             n += len(reviews)

#     # Combine existing reviews with new reviews
#     combined_reviews = existing_reviews + reviews_data

#     # Write the combined reviews data to a JSON file
#     with open(targetfile_path, 'w', encoding='utf-8') as json_file:
#         json.dump(combined_reviews, json_file, ensure_ascii=False, indent=4)

#     print(f'Scraped reviews have been appended to {targetfile_path}')


from googlemaps import GoogleMapsScraper
from datetime import datetime
import argparse
import json
from termcolor import colored
import os

ind = {'most_relevant': 0, 'newest': 1, 'highest_rating': 2, 'lowest_rating': 3}
HEADER = ['id_review', 'caption', 'relative_date', 'retrieval_date', 'rating', 'username', 'n_review_user', 'reviewer_image', 'url_user']
HEADER_W_SOURCE = ['id_review', 'caption', 'relative_date', 'retrieval_date', 'rating', 'username', 'n_review_user', 'reviewer_image', 'url_user', 'url_source']

def json_writer(ind_sort_by, path='data/'):
    outfile = ind_sort_by + '_gm_reviews.json'
    targetfile_path = path + outfile
    return targetfile_path

def serialize_review(review):
    """Convert review to a serializable format."""
    return {key: (value.isoformat() if isinstance(value, datetime) else value) for key, value in review.items()}

def load_existing_reviews(targetfile_path):
    """Load existing reviews from the JSON file if it exists."""
    if os.path.exists(targetfile_path):
        with open(targetfile_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    return []  # Return an empty list if the file does not exist

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Google Maps reviews scraper.')
    parser.add_argument('--N', type=int, default=100, help='Number of reviews to scrape')
    parser.add_argument('--i', type=str, default='urls.txt', help='target URLs file')
    parser.add_argument('--sort_by', type=str, default='newest', help='most_relevant, newest, highest_rating or lowest_rating')
    parser.add_argument('--place', dest='place', action='store_true', help='Scrape place metadata')
    parser.add_argument('--debug', dest='debug', action='store_true', help='Run scraper using browser graphical interface')
    parser.add_argument('--source', dest='source', action='store_true', help='Add source url to JSON file (for multiple urls in a single file)')
    parser.set_defaults(place=False, debug=False, source=False)

    args = parser.parse_args()

    # Prepare to write reviews to JSON file
    targetfile_path = json_writer(args.sort_by)
    
    # Load existing reviews to avoid duplicates
    existing_reviews = load_existing_reviews(targetfile_path)
    existing_review_ids = {review['id_review']: review for review in existing_reviews}  # Map review IDs to review objects

    reviews_data = []  # Initialize a list to hold review dictionaries

    with GoogleMapsScraper(debug=args.debug) as scraper:
        with open(args.i, 'r') as urls_file:
            for url in urls_file:
                if args.place:
                    print(scraper.get_account(url))
                else:
                    error = scraper.sort_by(url, ind[args.sort_by])

                    if error == 0:
                        n = 0

                        while n < args.N:
                            # logging to std out
                            print(colored('[Review ' + str(n) + ']', 'cyan'))

                            reviews = scraper.get_reviews(n)
                            if len(reviews) == 0:
                                break

                            for r in reviews:
                                review_id = r['id_review']  # Assuming 'id_review' is the key for the review ID
                                serialized_review = serialize_review(dict(r))  # Serialize the review data
                                
                                if review_id not in existing_review_ids:  # New review
                                    if args.source:
                                        serialized_review['url_source'] = url.strip()  # Add source URL if needed
                                    reviews_data.append(serialized_review)
                                else:
                                    # If the review ID already exists, compare the relative date
                                    existing_review = existing_review_ids[review_id]
                                    if existing_review['relative_date'] != serialized_review['relative_date']:
                                        print(colored(f"Updating review {review_id} due to relative date change.", 'yellow'))
                                        existing_review.update(serialized_review)  # Update existing review data

                            n += len(reviews)

    # Combine updated existing reviews with new reviews
    combined_reviews = list(existing_review_ids.values()) + reviews_data

    # Write the combined reviews data to a JSON file
    with open(targetfile_path, 'w', encoding='utf-8') as json_file:
        json.dump(combined_reviews, json_file, ensure_ascii=False, indent=4)

    print(f'Scraped reviews have been updated and saved to {targetfile_path}')
