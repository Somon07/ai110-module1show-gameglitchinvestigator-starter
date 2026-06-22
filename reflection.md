# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
 I inputted the number 10 and it kept telling me to go lower. For example when I inputted 9, it said to go higher, when the secret number was actually higher, 54.It seems as if the number was regenerating as it wasn't intialized in the session state.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
- The guess was not congruent with the actual secret number
- The guess function coded the hints backwards 



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 20    |      Go higher    |     Go lower    |  Code/logic error            |
|   9   |         Go higher  | Go lower       | Logic flaws |
| 54    |  Should say correct answer| It said go higher |Logic flaws |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I utilized Gemini and Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
   
   A suggestion it also gave me is when I asked why my secret number kept changing instead of being stored in its memory.It suggested that I input the target number into st.session_state to prevent Streamlit from wiping the application's memory. I reviewed this by going back and changing it and it remained stable.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---It suggested that the app kept giving me the wrong hints because of the Type Error block inside the check guess. I reviewed this to see that this was incorrect  when the app began comparing the numbers alphabetically instead of mathematically, resulting in backwards hints.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was fixed only after it passed in two places: an automated pytest test AND a live run of the game with streamlit. For the backwards-hint bug, I guessed 60 against a secret of 50 and confirmed the game now says go lower instead of "Go HIGHER!". I also moved the logic into logic.py so I could test the functions directly without launching the whole UI.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I added tests in test_gam.py. One test checks check_guess(60, 50) returns too high and that get_hint contains "LOWER". Another checks the scoring bug: update_score(100, "Too High", 2) must equal 95, because a wrong guess should never raise the score. All 6 tests passed which told me both the hint direction and the scoring were finally correct.

- Did AI help you design or understand any tests? How?
  Yes. The AI suggested splitting check_guess so it returns just the outcome string ("Too High") and a separate get hint returns the message. That made the starter tests pass and let me test the hint direction separately from the comparison logic. I verified this by running py_tests and watching all tests pass.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Streamlit works like a refresh button everytime that reloads from the start everytime. Utilizing session state to record your coding changes logs helps a lot.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to keep utilizing how to keep my bug finds and actual debugging results in a different place so it is more clear what my fixes wear and where I need to change the code to get better results

- What is one thing you would do differently next time you work with AI on a coding task?
I learned that a strategy I could be better on is learning how to reword my prompts to make my agent perform efficiently and give straightforward codes that work as efficiently as longwinded ones.
  
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I learned that using AI can help you learn more about the things you did not know instead of just using it for a solution, you can also use it to help guide you to the right answer.