# input sample data here
datastr = "26500 29473 22649 80591 63105 40290 53307 24284 50021 50563 34428 70108 69993 43305 23217 27690 50398 67645 78544 01674 33549 27883 93751 93286 72017 97563 54462 26899 48937 58526 21402 01591 23325 64977 38206 67709 00386 32548 64229 28433 26831 52358 32364 66338 11187 30076 31850 94956 69109 49987 16087 35336 93694 64050 35446 17614 50793 05962 95086 07565 99322 30221 37762 58175 36579 76190 51639 86198 68551 57155 03105 73720 05229 74392 94583 94721 80921 56227 47343 66640 99563 22101 09317 26934 05035 71628 87908 34641 76468 98662 07806 96947 48560 30359 93795 20741 56890 91235 78573 89184"  # input data into data string, separated by spaces

dataset = [int(num) for num in datastr.split()]
dataset_sorted = sorted(dataset)