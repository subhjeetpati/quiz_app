import requests

print("WELCOME TO QUIZ CENTER")
category = input("Choose the category by typing the number in front of the category\n1. General Knowledge\n2. Entertainment: Books\n3. Entertainment: Film\n4. Entertainment: Music\n5. Entertainment: Musicals and Theaters\n6. Entertainment: Television\n7. Entertainment: Video Games\n8. Entertainment: Board Games\n9. Science And Nature\n10. Science: Computers\n11. Science: Mathematics\n12. Mythology\n13. Sports\n14. Geography\n15. History\n16. Politics\n17. Art\n18. Celebrities\n19. Animals\n20. Vehicles\n21. Entertainment: Comics\n22. Science: Gadgets\n23. Entertainment: Japanese Anime and Manga\n24. Entertainment: Cartoons and Animations\n")
amount = input("Hpw many questions do you want to answer? (5 to 15)\n")



response = requests.get(f"https://opentdb.com/api.php?amount={int(amount)}&category={int(category)+8}&type=multiple")
points = 0

for i in range(int(amount)):
    print(f"{i+1}: {response.json()['results'][i]['question']}")
    options = []
    options.append(response.json()['results'][i]['correct_answer'])
    for j in range(3):
        options.append(response.json()['results'][i]['incorrect_answers'][j])
    options.sort()
    print(f"1.{options[0]} 2.{options[1]} 3.{options[2]} 4.{options[3]}")
    var = input("Choose the answer(1 to 4)\n")
    if options[int(var)-1] == response.json()['results'][i]['correct_answer']:
        print("Correct Answer")
        points += 1
    else:
        print(f"Wrong Answer. The Correct asnwer is {response.json()['results'][i]['correct_answer']}")

print(f"Your final score is {points} points out of {amount} ")
