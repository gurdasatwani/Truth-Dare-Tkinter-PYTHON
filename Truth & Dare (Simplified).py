# MODULES********************************
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

# *****************************************


# TRUTH & DARE LIST************************
truth_questions = [
    "Do you lie?",
    "What is the last thing you searched for online?",
    "Have you ever made out with someone who said you’re a bad kisser?",
    "Do you think you’re a good kisser?",
    "How many people have you kissed?",
    "Have you ever seen anyone “doing it” by accident?",
    "How would you rate your looks on a scale of 1-10?",
    "Who would you want to switch lives with out of everyone in this room?",
    "How did you first learn about “anatomy?”",
    "Do you lie about anything specific all the time?",
    "Do you pick your nose?",
    "Have you ever lied to someone you care about?",
    "Have you ever peed your pants?",
    "Have you ever gone #2 in your pants?",
    "What is your most embarrassing moment?",
    "Are you confident?",
    "Do you feel awkward peeing in front of others?",
    "Do you sing when no one is around?",
    "Do you dance alone when no one is there?",
    "Do you take a lot of selfies?",
    "Do you like being the center of attention?",
    "Have you ever thrown up in front of someone?",
    "Have you ever farted in front of someone and felt embarrassed?",
    "Do you have a crush?",
    "Who would you want switch lives with for an entire day?",
    "Who would you look like if you could look like any celebrity?",
    "Have you become a different person over the years?",
    "What has surprised you most in life?",
    "Have you ever ran out of toilet paper after using the bathroom?",
    "Do you think it’s wrong to pee in the shower?",
    "Have you ever had any accidental nudity?",
    "Ever sleep walk?",
    "Are you afraid of the dark?",
    "Do you take “naughty” pictures of yourself?",
    "How often do you check your texts?",
    "How often do you read the texts of someone who you like?",
    "Do you like anything nerdy?",
    "How often do you shower?",
    "Have you ever peed in a pool?",
    "What is the weirdest dream you’ve ever had?",
    "How often do you look in the mirror?",
    "Who are you most jealous of?",
    "Would you rather touch a snake or spider?",
    "Would you rather die young and happy or old and sad?",
    "Have you ever dealt with the death of a loved one?",
    "What is your biggest regret?",
    "If you could go back and re-do one year of your life, which would it be and why?",
    "Have you ever edited a picture to make yourself look skinnier?"
    "Have you ever eaten your feelings?",
    "Have you ever cried to get out of trouble?",
    "What website do you waste the most time on?",
    "Do you have any frenemies?",
    "Have you ever drunk dialed an ex?",
    "Have you ever tried to sabotage someone’s relationship?",
    "What is something no one knows about you?",
    "Have you ever hooked up with a friend’s ex?",
    "Have you ever done something to intentionally make your ex jealous?",
    "Have you ever done something cruel for no good reason?",
    "Have you ever chosen a guy over your friends?",
    "Which of your friends has the hottest boyfriend?",
    "What do you dislike most about your family?",
    "What is your worst habit?",
    "What makes you cry?",
    "What is the scariest thing you’ve ever done?",
    "Who would you cast to play you in a movie?",
    "What’s your weirdest habit?",
    "Have you ever gone to third base?",
    "Have you ever played spin the bottle?",
    "What is the meanest thing you’ve ever done?",
    "Name one thing you love about everyone in the room",
    "What is the strangest dream you’ve ever had?",
    "What makes you sad?",
    "Can you tell me 5 traits about yourself you like?",
    "What was the worst part of your childhood?",
    "Have you ever cheated on an important test?",
    "What is your “dream job?”",
    "Have you ever edited a picture on social media?",
    "Do you stalk the social media of people you like?",
    "Who do you think is the prettiest girl here?",
    "Do you have any hidden talents?",
    "Who do you think is the best looking guy at school?",
    "Who is someone you hooked up with and totally regretted it?",
    "When was you first kiss?",
    "Have you ever told a secret that you swore you wouldn’t tell anyone?",
    "What is the meanest thing anyone has ever said to you?",
    "What is the meanest thing you have ever said to or about someone?",
    "Have you ever practiced kissing on your hand?",
    "Have you ever prank called someone?",
    "Have you ever broken someone’s heart?",
    "Ever had your heart broken?",
    "Craziest person you’ve gone on a date with?",
    "Do you have any celebrities you are obsessed with?",
    "Ever lied about being sick to get out of school?",
    "If you could make one wish, what would it be?",
    "If you won $ 1 billion what would you do with it?",
    "Have you ever lied about your age?",
    "What’s an embarrassing song you like?",
    "Have you ever dreamed of being famous?",
    "Have you ever lost your keys?",
    "Who is your spirit animal?",
    "Have you ever kissed a girl before?",
    "Have you ever kissed a boy before?",
    "Have you ever gone to second base?",
    "Have you ever walked in on someone having sex?",
    "What’s the longest you’ve gone without showering?",
    "Have you ever flashed someone?",
    "Who is your least favorite person here?",
    "What is your greatest fear?",
    "How many people have you made out with?",
    "Have you ever sent a nude selfie?",
    "Do you think you’re pretty?",
    "What is the biggest lie you’ve ever told?",
    "What was your biggest childhood fear?",
    "Are You A Gay?",
    "Are You A Lesbian?",
    "Are You A Gold Digger?",
    "Have you ever stolen?",
    "When did you lose your virginity?",
    "What would you do if you got pregnant?",
    "Have you ever done something illegal?",
    "Have you ever made out in the back of a car?",
    "Who are you interested in right now”",
    "Would you rather date X or Y?",
    "Have you ever had a crush on a teacher?",
    "What has been your most embarrassing moment in school?",
    "Who is your favorite male celebrity?",
    "Who is your favorite Instagram star?",
    "Are you afraid of heights?",
    "What’s your GPA?",
    "What’s something your parents don’t know?",
    "Have you ever pulled a prank on a teacher?",
    "When was the last time you got grounded and what was it for?",
    "Do you have a fake ID?",
    "Have you ever snuck out of the house?",
    "How many detentions have you had?",
    "Have you ever asked a guy out and been rejected?",
    "Have you ever loved someone who didn’t love you back?",
    "Have you ever had a crush on your friend’s boyfriend?",
    "Do you secretly hate any of your friends’ boyfriends?",
    "Have you ever sent a “bad” picture on Snapchat?",
    "Have you ever lied about sleeping with a guy?",
    "Could you survive without your phone for a week?",
    "Have you ever spread a rumor about someone?",
    "Have you ever lied to a teacher?",
    "Have you ever been drunk?",
    "Have you ever used Tinder?",
    "How much makeup do you wear?",
    "What’s your favorite form of social media?",
    "Have you ever borrowed something from a friend and not given it back?",
    "Have you ever gone on a starvation diet?",
    "Have you ever had a crush on someone ten years older?",
    "Who do you want to go to prom with?",
    "Have you ever copied someone’s homework?",
    "What is your best “the dog ate my homework” excuse for not handing something in on time?",
    "Have you ever smoked?",
    "Who of your friends has the worst Instagram account?",
    "Who of your friends sends the most annoying snapchats?",
    "Does going away to college make you nervous?",
    "What is the worst rumor that has ever gone around about you?",
    "Have you ever fooled around with someone at school?",
    "Have you ever failed a test?",
    "Have you ever been suspended?",
    "Who is the hottest teacher at school?",
    "How many people have you kissed?",
    "What do you like most about yourself?"
    "If you could be a Disney princess, who would it be and why?",
    "Do you feel jealous of people who have tons of followers on social media?",
    "Do you think being Instagram famous is pathetic or cool or neither?",
    "Should weed be legal?",
    "Are you open-minded?",
    "Do you think social media is bringing people closer together or making everyone more isolated and alone?",
    "Do you know anyone with an addiction?",
    "Have you ever struggled with addiction?",
    "Do you think hair extensions are tacky?",
    "What is something you hate about your job?",
    "Do you think Tinder is ruining society?",
    "Do you think you’re living a lie?",
    "How often do you check your social media?",
    "Who did you vote for?",
    "Do you believe in marriage?"
    "Do you believe in monogamy?"
    "What’s your biggest pet peeve?",
    "Have you ever dated multiple people at the same time?",
    "Do you ever intentionally not respond to someone to keep them guessing?",
    "What’s your craziest political view?",
    "Have you ever taken a picture down from Instagram because it didn’t get a lot of likes?",
    "Have you ever gone on a march/protest?",
    "If you were given a million dollars, what would you do with it?",
    "What makes you irrationally angry?",
    "What would you do if you had an STD but your partner did not know?",
    "Tell Us Your Crush Name?",
    "Describe the weirdest date you’ve ever gone on.",
    "Smallest …. size you’ve been with?",
    "Have you ever tried to hook up with a guy you knew had a girlfriend?",
    "Have you ever cheated on someone?",
    "Have you ever been cheated on?",
    "What is the most romantic thing a guy has ever done for you?",
    "Have you ever dated someone shorter than you?",
    "Worst first date story?",
    "Have you ever flirted your way out of trouble?",
    "Have you read “50 Shades of Grey?”",
    "Do you think it’s annoying that most women edit their social media profiles and post fake pictures?",
    "Have you ever used Tinder?",
    "What is one makeup item you can’t live without?",
    "Would you ever hook up with a member of the same sex?",
    "How often do you check your “ex’s” online social media if ever?",
    "Do you secretly love any of your exes still?",
    "How many guys have you been with?",
    "When was the last time you “pleasured yourself?”",
    "How often do you weigh yourself?",
    "Are you happy with your weight?",
    "Do you dye your hair?",
    "Do you wear a lot of makeup?",
    "Would you ever walk around all day without makeup on?",
    "What is your biggest insecurity?",
    "How often do you workout?",
    "Have you ever lied to a guy about your weight?",
    "Who is your favorite male celebrity?",
    "What’s your favorite body part?",
    "Do you like your boobs?",
    "Would you ever get any plastic surgery?",
    "Do you think getting plastic surgery is cheating?",
    "Have you ever taken drugs to be skinny?",
    "Have you ever been on any kind of antidepressant or psychiatric medication?",
    "Have you ever had a pregnancy scare?",
    "Have you ever done botox?",
    "Have you ever done it on the first date?",
    "Do you ever go commando?",
    "Have you ever lied to impress a guy on a date?,Have you ever lied to a woman?",
    "Have you ever dyed your hair?",
    "What was your honest first impression of your significant other?",
    "Are you afraid of going bald someday?",
    "What’s your wildest fantasy?",
    "Have you ever had an STD?",
    "What is your go-to pickup line?",
    "Do you think you are attractive?",
    "Do you hide anything from the world?",
    "Have you ever cheated on someone?",
    "What is something you’re embarrassingly bad at?",
    "Has a girl ever slapped you across the face?",
    "Have you ever gotten a girl pregnant?",
    "If you got someone pregnant, would you want them to get an abortion?",
    "How often do you “do yourself?”",
    "Do you think all girls are “crazy”?",
    "What’s the craziest thing a girl has done for you or to you?",
    "What’s your strangest sexual experience?",
    "Do you actually enjoy “adult entertainment”?",
    "Tell me your most embarrassing moment of your life.",
    "Who are you most jealous of?",
    "Have you ever questioned your sexuality?",
    "Do you enjoy sports?",
    "Have you ever pretended to enjoy sports?",
    "Have you ever pretended to like a show because it is popular?",
    "Which animal would you be: a lion or a puppy?",
    "When was the last time you cried?",
    "How big is your… you know what?",
    "Have you ever “measured” your.. you know what?",
    "Do you prefer blondes, brunettes, or redheads?",
    "If you could hook up with one of your friend’s girlfriends, who would it be?",
    "What is your biggest turn-on?",
    "What is your biggest turn-off?",
    "Have you ever ghosted on a girl?",
    "Have you ever been in a fist fight?",
    "Have you ever lied about the number of women you’ve been with?",
    "Have you ever been attracted to another man?",
    "Have you ever had the hots for your friend’s girlfriend?",
    "What is the most superficial reason you broke up with a girl?",
    "Have you ever hooked up with one of your girlfriend’s friends?",
    "Have you ever lied to get a woman into bed?",
    "Do you have any feminine qualities?",
    "What is your biggest fear when it comes to relationships?",
    "Do you enjoy fighting?,Who is the hottest person in this room?",
    "Do you care more about sex or love?",
    "What is the most embarrassing thing you’ve done when drunk?",
    "Who would you choose to hook up with if you had to pick one person in this group?",
    "Who would you most likely want to have sex with?",
    "What’s the wildest thing you’ve ever done?",
    "Have you ever sent an embarrassing text to someone by accident? Describe",
    "What was the worst sex you’ve ever had?",
    "Would you rather hook up with X person or Y person?",
    "Biggest fear right now?",
    "Have you ever done illegal drugs?",
    "Have you ever had a one night stand?",
    "Who has the best butt in the room?",
    "Who has the best boobs in the room?",
    "Which friend is hotter… X friend or Y friend?",
    "Would you rather be friends with X person or Y person?",
    "Who is the most annoying person here?",
    "Would you rather be poor or ugly?",
    "Who looks like they would be terrible in bed?",
    "Who looks like they would be amazing in bed?",
    "Who is someone you know that really need to lay off the alcohol?",
    "List the most attractive quality of every person playing this game.",
    "Who here do you think would be the best kisser?",
    "Marry, sleep with, kill- pick someone for each category.,When was the last time you “did yourself?”",
    "Craziest drunk story?",
    "Greatest fear?",
    "Are you a hopeless romantic?",
    "Can you tell me something you’ve never told anyone else?",
    "Do you like anyone right now?",
    "Tell me a secret.",
    "Do you hate anyone?",
    "What is your worst memory?",
    "Have you ever thrown up from drinking?",
    "What is your secret you would never tell anyone?",
    "Have you ever felt humiliated?",
    "When was the last time you cried?",
    "What is the one app on your phone you can’t live without?",
    "What do you wish you could change about your life?",
    "Have you ever not texted a girl back instead of just breaking up with her?",
    "Have you ever sent a dirty picture on snapchat?",
    "What is something a girl can do that makes her instantly unattractive?",
    "What makes someone girlfriend material?",
    "Have you ever stalked anyone on social media?",
    "Do you stalk your exes on social media?",
    "If you could marry a movie character, who would it be?",
    "What is one thing you can’t live without?",
    "What or who annoys you the most?",
    "Have you ever blamed someone for something you did?,Do you think we have a purpose on this planet?",
    "Do you believe time might not actually be linear?",
    "Is life meaningless or meaningful?",
    "Does heaven exist?",
    "Where do we go when we die?",
    "Do you believe in God?",
    "If you died tomorrow would you have regrets?",
    "Do you think you’re capable of killing someone?",
    "Do you believe in soul mates?",
    "What is love in the first place?",
    "Can you love one person forever?",
    "What do you believe in?",
    "Is it wrong to cry?",
    "Do you believe in karma?",
    "Do you think there is an after life?",
    "Have you ever had an out of body experience?",
    "Have you ever had a near death experience?",
    "Does everything happen for a reason?",
    "Do you believe love conquers all?",
    "Finish the sentence: the world would be a better place if ____",
    "Do you feel like you have a purpose in life?",
    "Who is your favorite family member?",
    "What is your least favorite part about family gatherings ?",
    "What is the biggest secret that you kept from your parents when you were growing up?",
    "What is your favorite movie that you secretly know is actually terrible?",
    "What is your worst habit?",
    "Have you ever bribed or flirted with a police officer to get out of a ticket?",
    "What is something you most look forward to doing when you retire?",
    "Do you have a bucket list?If so, what is one thing on that list?",
    "What is one thing you are always losing?",
    "What is the strangest thing you have ever bought?",
    "Do you have a weird collection?If so, what?",
    "Tell us about the last dream you can remember. Don’t leave any details out!",
    "Have you ever shared chewing gum with anyone?",
    "Have you ever lied about being sick so you could stay home from work or school?",
    "If you could do one thing you did when you were a child, what would it be?",
    "Have you ever danced on a table when you were drunk?",
    "Have you ever told someone you wouldn’t be home just so they wouldn’t come over to yours?",
    "What is the one thing you dislike about yourself?",
    "What is the one thing you really like about yourself?",
    "What is the one thing you would stand in line for?",
    "Have you ever lied on your resume to get a job?",
    "If anyone in your family could win an award for being the most annoying, who would it be?",
    "What is the most embarrassing thing that has happened to you in front of a crowd?",
    "What is your least favorite household chore?",
    "If you could hire someone to do one thing for you, what would it be?",
    "What was the most embarrassing thing that you ever did while on a date?",
    "What was the worst gift you ever received?",
    "What is the one thing you are the most afraid of?",
    "Have you ever sent an inappropriate text to your mom or dad by accident?",
    "Have you ever bought something to wear to an event and then returned it to the store when the event was over?",
    "Have you ever fallen asleep in church?",
    "Did you ever break up with someone just before a public holiday so that you didn’t have to buy them a gift?",
    "Have you ever kept a library book?",
    "Have you ever cheated on a test?",
    "If you could create your own job title, what would it be?",
    "What is your excuse to get out of exercising?",
    "What was the one thing you could never learn how to do no matter how hard you tried?",
    "What was your favorite childhood television show?",
    "Did you ever sneak into an adult movie when you were underage?",
    "If you had a remote control that would operate anything, what would you control?",
    "Have you ever complained about something at a restaurant just to get out of paying?",
    "What is one thing you did as a child that you still enjoy?",
    "Do you prefer the big city or country life?",
    "What is your guilty pleasure?",
    "What are your favorite pizza toppings?",
    "Where is your favorite vacation spot?",
    "Have you ever used a work computer for personal use?",
    "What is your favorite thing to do with your leisure time?",
    "What was the worst vacation you ever had?",
    "If you were to bury a time capsule, what is one thing you would put in it?",
    "If you were granted three wishes, what would they be?",
    "What is your favorite holiday?",
    "What is your biggest pet peeve?",
    "If you could choose a different career, what would it be and why?",
    "If you could live anywhere in the world, where would it be?",
    "What is your favorite snack from a vending machine?",
    "Have you ever forgotten a special person’s birthday?",
    "Have you ever taken a drink straight out of the carton?",
    "On a scale from 1-10, where does your patience fall?",
    "If animals could talk, which one would you have a conversation with?",
    "Tell us about the worst restaurant experience you ever had.",
    "Is there any movie that always makes you cry?",
    "Say the funniest joke you’ve ever heard.",
    "What is something you find absolutely disgusting to the point you get sick?",
    "Have you ever been stuck in an elevator and if so who were you with?",
    "Have you ever been on an airplane and if so where were you going?",
    "Who was your favorite teacher in school?",
    "What was your favorite subject in school?",
    "What is something that you are not looking forward to?",
    "Knowing now what you didn’t know then, what would you have done differently?",
    "Have you ever told a secret after you were told not to?",
    "Are you always on time, or are you always late?",
    "Are you a morning person or a night person?",
    "What is one job you would never want to do?",
    "What is your favorite ice cream flavor?",
    "When you think that no one is listening, do you sing in the shower?",
    "The last time you argued with someone, did you apologize first or was it the other person?",
    "What is the best gift you ever received?",
    "Is there any food that you can never eat?",
    "What was your favorite childhood toy?",
    "If you were given a million dollars, what would you do with it?",
    "Have you ever been arrested?",
    "What is your favorite sport?",
    "Have you ever been golfing?",
    "Have you ever played tennis?",
    "What is your favorite ride at the amusement park?",
    "Do you prefer the beach or the mountains?",
    "Have you ever been on a train?",
    "If you found a large amount of money, would you keep it or would you try to find the owner?",
    "What is the angriest you’ve ever been?",
    "What makes you the happiest?",
    "What is your favorite sandwich?",
    "Is there anything you regret buying, and if so, what is it?",
    "What is the best thing you ever bought?",
    "If you were invisible what is something you would do?",
    "What makes you feel uncomfortable?",
    "Do you prefer cats, dogs, or neither?",
    "If there was one thing you could change about yourself, what would it be?",
    "If you were a giant, what would you like to do?",
    "What is your favorite music genre?",
    "Have you ever blamed your sibling for something you did just so that you wouldn’t get in trouble?",
    "How old were you when you got your first cell phone?",
    "When is the last time you took a shower?",
    "When is the last time you brushed your teeth?",
    "Describe your favorite activity when you’re alone.",
    "What do you like to do when you are with your friends?",
    "Who was your first crush?",
    "How old were you when you had your first crush?",
    "What is the best time of day for you?",
    "What is your least favorite time of the day?",
    "If you didn’t have to work, what would you do with all your time?",
    "Tell us about your favorite possession.",
    "Name the three websites you visit the most.",
    "What was the best day you ever had?",
    "Describe the worst day you’ve ever had.",
    "Say your biggest fear in life.",
    "Did you have a nickname as a child and if so, what was it?",
    "Do you prefer mushy movies or funny ones?",
    "If you only had two minutes to get out of your house, what would you grab?",
    "What is your favorite vegetable?",
    "What is your favorite fruit?",
    "Do you have a special talent and if so, what is it?",
    "Have you ever been married?",
    "What do you like to put on your toast?",
    "What is the spiciest thing you’ve ever eaten?",
    "If you could live anywhere in the world, where would it be?",
    "Do you prefer Facebook or Twitter?",
    "What season is your favorite?",
    "Who is your most annoying neighbor?",
    "If you could be someone else for a day who would you be?",
    "What was the name of the street you grew up on?",
    "Which do you like better, cars or trucks?",
    "What is your favorite outdoor pastime?",
    "Which do you like better, Coca-Cola or Pepsi?",
    "What is your favorite month and why?",
    "Do you like to read and if so, what is your favorite book?",
    "Have you ever met a celebrity, if so, who?",
    "Has there have been a time when you cheated to win a game?",
    "Have you ever sent a love message to your boss by accident that was meant for someone else?",
    "What food do you absolutely despise?",
    "Who is the person you are the most jealous of and why?",
    "How many different languages can you speak and what are they?",
    "Do you have any tattoos and if so, where?",
    "Have you ever been outside of the country?",
    "What is one thing your grandparents taught you how to do?",
    "Have you ever been to the opera?",
    "Do you prefer talking or texting?",
    "Have you ever had an argument with someone through text?",
    "What was the last thing you ate?",
    "Have you ever been to the zoo?",
    "What is the grossest thing you’ve ever eaten?",
    "What is your most regrettable kiss?",
    "Have you ever failed a test?What was it?",
    "Who is your favorite teacher and why?",
    "Who was your longest secret crush?",
    "Where do you like to go when you’re feeling down?",
    "What is your favorite song?",
    "Who would you rather live with: Miley Cyrus, Snoop Dogg, or Adam Levine?",
    "What is something you have never told anyone in this room?",
    "What do you like to wear when no one is around?",
    "Who would rather be stuck on a desert island: the person on your left or on your right?",
    "For parents: which is your favorite child?For children: which is your favorite parent?",
    "Who would you rather marry: Brad Pitt, Zach Efron, or Antonio Banderas?",
    "Have you ever shoplifted or stolen anything?",
    "Describe the worst date you’ve ever been on.",
    "If you could be fluent in one of these languages which would it be: Chinese, French or Russian?",
]
dare_question = [
    "Drink a weird combination of: ketchup and mustard and something else (nothing that will send people to the emergency, please!)",
    "Go on Facebook and write a really long rant.",
    "Try counting backwards from 100 in multiples of three.",
    "Do a handstand.",
    "Do a cartwheel.",
    "Do a downward dog.",
    "Do an impression of everyone in the room",
    "Drink hot sauce.",
    "Go next door and ask the neighbor for 1 egg and half a teaspoon of sugar",
    "Don’t speak for half an hour!",
    "Hop on one leg for 5 minutes.",
    "Call a random number and pretend to be someone else.",
    "Do a weird dance in front of everyone.",
    "Let everyone draw on your face.",
    "Sing a song for everyone.",
    "Let everyone give you a makeover.",
    "Scream out the window while driving.",
    "Harass people in an online fight.",
    "Touch your toes.",
    "Make out with your hand",
    "Fake cry.",
    "Slap yourself in the face.",
    "Go through a garbage can.",
    "Pick someone’s nose",
    "Eat a spoonful of salt",
    "Drink a mouthful of water and try to keep it in your mouth as the group shares funny stories.",
    "Show Your Crush Social Media Account.",
    "Strip naked and dance.",
    "Call your mom and ask her how much she would charge for a “pleasurable favor” and mask your caller ID. Use a foreign accent.",
    "Pretend to “drunk dial” your ex and say “meow bear.”",
    "Drink an entire bottle of soda.",
    "Let us blindfold you and tickle you!",
    "Get naked and run around the room.",
    "Make out with a vegetable.",
    "Eat an entire box of cereal.",
    "Drink a liter of soda.",
    "Jump up and down and tell a story.",
    "Make up a dance.",
    "Pretend you’re a mermaid.",
    "Don’t speak for 10 minutes.,Text X person something crazy",
    "Go on Facebook and type “I love boobs.”",
    "Make a really ugly cry face.",
    "Tell your crush you like them.",
    "Tell a fake story about a man named Ben.",
    "Say something extremely politically incorrect about someone you hate.",
    "“Moon” us.",
    "Show us your phone and let us go through it for five minutes.",
    "Let us read your Facebook messages.",
    "Let us read your Snapchat.",
    "Walk on all fours as if you’re a dog.",
    "Call the last person in your call history and talk in a foreign accent. Then hang up.",
    "Call two people from your contact list and start “meowing” at them. Then laugh and hang up.",
    "Do your best Britney Spears imitation.",
    "If you’re a guy, put on makeup.",
    "If you’re a girl, take off all makeup.",
    "Post an unfiltered, unattractive selfie on social media",
    "Go to Youtube, find a live chat and start a fight.",
    "Call a local pharmacy and ask if they have herpes medication.",
    "Post something politically controversial on Facebook.",
    "Post a comment on every single post on the first page of your Facebook feed.",
    "Go on Facebook Live and talk about how much you love pizza for five minutes,Go hit on a man with a cheesy pickup line.",
    "Take all your makeup off.",
    "Let us have your phone to go through.",
    "Let us see your texts.",
    "Show us what’s in your purse.",
    "Stand outside your house for a second in your underwear.",
    "Fake an orgasm.",
    "Drop a piece of jewelry into the toilet and then pick it up.",
    "Post a rant about feminism on Facebook.",
    "Rank your friends from most to least attractive.",
    "Scream as loud as you can.,Do your best Michael Jackson impression.",
    "Put on women’s underwear.",
    "Call a drugstore and ask if they carry male period tampons.",
    "Knock on your neighbor’s door and yell at them.",
    "Call your best friend and ask if he enjoyed himself in the brothel last night using a blocked caller ID And speaking in a foreign accent.",
    "Go outside in just your boxers and dance for 1 minute.",
    "Do 20 push-ups.",
    "Go outside in just underwear and do the Macarena.",
    "Kiss the floor.",
    "Throw a football.",
    "'Drink a weird recipe of ketchup and mayonnaise.",
    "Get in your car and do a “donut” peeling out of the house (warning: don’t get arrested).",
    "Shave your armpits",
    "Sing My Heart Will Go On with hand motions",
    "Recite a love poem to the most attractive girl in the room",
    "Talk like a girl for the rest of the game",
    "Kiss the person to your right on the neck",
    "Do a dance to the song “I’m too sexy.”",
    "Let someone wax a part of your body.",
    "Attempt to breakdance.,Kiss the person next to you.",
    "Make out with the person across from you.",
    "Start hopping on one leg.",
    "Pretend you can’t talk and try to make a sentence using your body.",
    "Go poke someone and walk away.",
    "Lick the person nearest to you.",
    "Lay on X person’s lap.",
    "Dance alone for 15 minutes.",
    "Jump up and down for 5 minutes.",
    "Give the person to your right a foot massage.",
    "Blindfold yourself and take a shot of whatever we choose.",
    "Take your bra off and keep it off for the rest of the game.",
    "Start twerking in the middle of the room.",
    "Drink a glass of wine as if it’s water.,Do 15 jumping jacks.",
    "Pretend to be a ballerina.",
    "Put on a weird hat and make faces in the mirror.",
    "Lie down and pretend you’re a fish.",
    "Do your best impression of a president.",
    "Bark like a dog for a minute.",
    "Sing like no one is watching.",
    "Make up a rap.",
    "Pick someone’s nose.",
    "Switch pants with someone of the opposite sex.",
    "Pet someone as if they are a pet.",
    "Crack an egg over your head",
    "Tell someone you’re pregnant (if you’re a woman). And if you’re a guy tell someone you got a girl pregnant.",
    "Eat a rose petal or some kind of flower.",
    "Throw rocks at someone’s window gently (don’t hurt anyone!)",
    "Talk only in animal sounds for the next 30 minutes.",
    "Put on a blindfold and let the person next to you draw on you.",
    "Let everyone draw on your back.",
    "Call a radio station and say random things.",
    "Do the cinnamon challenge",
    "Go outside and do a rain dance",
    "Speak only in rhyme",
    "Go live on Facebook and sing “Let It Go” on the top of your lungs",
    "Paint your eyebrows with peanut butter",
    "Dance without music on for a full minute.,Touch me anywhere you want.",
    "Take one article of clothing off of me. You decide.",
    "Stare at me with my top off for two minutes without touching me.",
    "Stare at me without any “bottoms” on but don’t touch me.",
    "Get naked and let me stare at you.",
    "Do anything you want to me.",
    "Lick whipped cream off my body",
    "Take a naked selfie and send it to your significant other",
    "Do a sexy striptease",
    "Completely cover yourself in toilet paper to look like a mummy.",
    "Randomly call a person from your phone and sing them a song.",
    "Call a family member of someone in the room and explain why you love your friend so much.",
    "Run outside and shout as loud as you can, “I am the best person in the world!”",
    "Mix all the sauces you have in your fridge and drink up.",
    "Prank call a friend’s partner.",
    "Call up a pizza place and order Chinese food.",
    "Take a shower without removing any of your clothes.",
    "Cover up your eyes (or wear a blindfold), and walk around the room for two minutes without watching where you’re going.",
    "Impersonate someone in the room and people have to guess who it is.",
    "Improvise and perform a two-minute comedy routine in front of everyone.",
    "Act like a dog for two minutes without laughing.",
    "Pour a freezing cold glass of water over your face without reacting.",
    "Talk about something you regret in your life.",
    "Tell a stranger walking past that you love them.",
    "Put as many pieces of cheese puffs in your mouth at one time as you can.",
    "Screenshot a picture of your browser history and send it to a random person in your contacts.",
    "Log into Facebook and like every picture for the past year of the first person you see.",
    "Rip off a piece of paper and eat it.",
    "Take out an eat and eat it raw.",
    "Cover your hair with milk and don’t wash off until the end of the game.",
    "Text your mom the last picture saved on your phone.",
    "Pretend to be a chicken for 30 seconds.",
    "Stand up and run on the spot as fast as you can until it’s your turn.",
    "Sniff the player to your right’s armpit.",
    "Allow another player to throw flour in your face.",
    "Allow a random player to tickle you for 30 seconds.",
    "Kiss someone’s bare foot.",
    "Go into the kitchen and take a bite out of something in the trash.",
    "Spritz perfume into your mouth.",
    "Head outside and lick a car tire.",
    "Take a picture of yourself pulling a funny face and set it as your Facebook profile picture for the rest of the day and night.",
    "Pass your phone to the person to your right and allow them to put any status on one of your social media accounts.",
    "Let someone in the group give you a wedgie.",
    "Grab a random object in the room and try and sell it to the group for two minutes.",
    "Kiss the second person to your left on the lips.",
    "Sing the chorus from a random song with all your heart.",
    "Speak in a baby’s voice for the next five things you have to say.",
    "Give someone in the group all the money you have in your purse.",
    "Take someone’s socks off and wear them like gloves for three minutes.",
    "Slap yourself in the face any time someone says “and” in the next three minutes.",
    "Blindfold yourself and let someone in the group feed you something of their choosing.",
    "Knock on your neighbor’s door and tell them how grateful they should be to live next to someone so awesome.",
    "Try to lick your elbow for the next three minutes.",
    "Laugh out loud at everything the person to your left says until it’s your turn.",
    "Stand up and try to break dance.",
    "Try to impersonate your favorite singer for one minute.",
    "Pick out the best and worst dressed individuals in the group.",
    "Act like you’re drunk for the rest of the game.",
    "Hum a random song and you can’t stop until someone guesses what it is.",
    "Let someone bite your finger until it hurts.",
    "Attempt to keep your eyes as wind open as possible without blinking.",
    "Open a book, newspaper or magazine, and sing two random sentences as best you can.",
    "Show everyone the four most recent pictures on your phone.",
    "Write and perform a song that is at least two minutes long.",
    "Ring a random person from your phone and confess that you’re in love with a fictional character.",
    "Hold your breath for as long as you can.",
    "Apply makeup without looking in the mirror.",
    "Let a player write something on your head and don’t wipe it off until the end of the game.",
    "Hold a plank for as long as you can.",
    "Do as many sit-ups as you can in one minute.",
    "Trade one item of clothing with another player and wear for the rest of the game.",
    "Try to sing a song with your mouth full of a drink.",
    "Eat a spoonful of a spicy sauce.",
    "Hold mouthwash in your mouth for as long as possible (extra minty flavors work best for this!).",
    "Let any player give you a wet willy.",
    "Allow the second player to your right to make an alcoholic drink and you have to drink it as fast as you can.",
    "Completely shave off one of your eyebrows.",
    "Let someone wax half of your leg.",
    "Nibble at another player’s fingernails.",
    "Go outside and ask a stranger to smell your breath.",
    "Eat an entire onion without crying.",
    "Allow another player to cut a small chunk out of your hair.",
    "Massage another player’s back for five minutes.",
    "Sit among other players wearing only your underwear.",
    "Let another player keep any item of clothing from your wardrobe.",
    "Try to juggle with three eggs.",
    "Spank the person to your right.",
    "Confess your undying love to another player in the room.",
    "Blindfold yourself and allow another player to feed you something of their choosing, and you’ve got to guess what it is.",
    "Smell someone else’s shoes for one minute.",
    "Text the last person you called saying, “I love you”.",
    "Speak in an accent chosen by another player for the rest of the game.",
    "Streak around the room for 10 seconds.",
    "Sit on someone else’s lap for five minutes.",
    "Allow another player to search anything they want on your phone.",
    "Eat an item of food off of someone’s face without using any hands.",
    "Passionately kiss the back of your hand and let someone record it.",
    "Describe someone else in the group and others have to guess who it is.",
    "Tell everyone about an embarrassing crush you once had.",
    "Grab a broom and pole dance on it until someone tells you to stop.",
    "Whisper a secret about yourself to another player in the group.",
    "Perform your best air guitar routine without any music playing.",
    "Twerk wearing only your underwear.",
    "Let another player crack an egg on your head.",
    "Dress up like the opposite sex and let another player take a picture and upload it online.",
    "Put honey on the end of your house and then apply flour, and keep it like that for the rest of the game.",
    "Put an ice cube down your pants and let it melt.",
    "Pretend that you’re a cat and rub up against the other players for one minute.",
    "Say the entire alphabet backward.",
    "Go to a neighbor’s house and ask if they have any spare food because you’re hungry.",
    "Make up a two-minute rap about an inanimate object in the room.",
    "Paint your fingernails with the nail varnish in your mouth.",
    "Call the tenth contact on your phone and tell them all about your day, for no apparent reason.",
    "Head outside and talk to a random stranger as if they’re an old friend you haven’t seen in years.",
    "Balance an object on your head while walking around the room for one minute.",
    "Let the player to your left give you a new hairstyle for the rest of the game.",
    "Tell everyone an embarrassing story about yourself.",
    "Take a mouthful of water and tell a funny story about something that’s recently happened to you.",
    "Get down on one knee and pretend to propose to another player.",
    "Sing everything you want to say for the next 10 minutes.",
    "Eat as many pieces of bread as you can in two minutes.",
    "Lick a bar of soap from the bathroom.",
    "Text your mom and tell them you’re pregnant, or if you’re a boy, say that you’re going to be a dad.",
    "Go outside and carry a sign that says “kiss me if you think I’m attractive”.",
    "Take a bite and swallow a piece of a banana skin.",
    "Lick an animal’s fur.",
    "Pretend that you’re a sheep for no reason whatsoever.",
    "Write a poem about why you are the best person in the world.",
    "Take a selfie with some old trash.",
    "Spank the closest person to you.",
    "Prank call your ex and tell them that you want to get back together.",
    "Eat a sandwich filled with ingredients chosen by other players.",
    "Put a teaspoon of salt in your mouth.",
    "Consume as many chilies as you can in two minutes.",
    "Head outside for a walk and talk aloud to yourself.",
    "Tell a stranger that you’re having a bad day and need someone to talk to.",
    "Lick the floor.",
    "Go outside and wink at the first person you see.",
    "Dance outside for two minutes without any music playing.",
    "Tell everyone about a celebrity crush you have.",
    "Take a picture of yourself pulling a funny pose and upload it to social media.",
    "Call a random person and wish them a happy birthday.",
    "Run around the house wearing someone else’s underwear on your head.",
    "Have a conversation with the TV.",
    "Act like you’re a child for two minutes.",
    "Let another player do whatever they want to your feet.",
    "Lick sauce off of someone else’s armpit.",
    "Brush your teeth with hot sauce.",
    "Drink an entire bottle of milk to yourself.",
    "Laugh like a hyena to everything everyone says until it’s your turn.",
    "Prank call a car breakdown company and say that you’re sad because you don’t have a car.",
    "Do your best impersonation of Elvis Presley.",
    "Send a direct message to the last person you wrote to on Instagram saying that they’re beautiful.",
    "Dye your hair a color of a player’s choosing.",
    "Clean another player’s bathroom when it next needs doing.",
    "Give a stranger five dollars.",
    "Wash another player’s feet.",
    "Dip your hand in toilet water.",
    "Apply lipstick to your mouth and teeth and walk outside.",
    "Chug a glass of milk with curry powder.",
    "Do a handstand with your feet against the wall and hold for 30 seconds.",
    "Give your phone to the person on your left and let them send any message they want to anybody on your contact list.",
    "Let the person to your right give you a temporary marker tattoo on your forehead of anything they want.",
    "Call your sibling or cousin and speak to them for one minute entirely in an Italian accent.",
    "Spell out your name on the wall with your butt (don’t use markers, it’s invisible).",
    "Do the entire Gangnam Style dance using headphones so no one else hears the song.",
    "Sing your country’s national anthem while plugging your nose.",
    "Choose one other player and dance to the Titanic theme song while holding an orange between you (no hands). Don’t let the orange fall!",
    "Call your neighbor and make monkey sounds for 30 seconds straight.",
    "Call the most recent food delivery number that you have dialed and sing them the Happy Birthday song.",
    "Make a love declaration to the player sitting opposite you.",
    "Do a belly dance to the tune of Ricky Martin’s “La Voda Loca”",
    "Pick the nose of the oldest person in the room.",
    "Email your favorite teacher and tell them you love them.",
    "Put a Skittle or M&M in the belly button of the person across from you and eat it.",
    "Propose to the last person you sent a text message to.",
]
# *****************************************


# MAIN************************************


main = Tk()
main.configure(bg="black")


# QUIT BUTTON*****************************
quit = Button(main, bd=5, bg="black", fg="white", text="QUIT", command=main.destroy)
quit.pack()
quit.place(x=-1, y=1400)
# *****************************************


# GAME NAME******************************
lable0 = Label(
    main, text="TRUTH", bg="black", fg="green", font=("Helvetica", 23, "bold", "italic")
)
lable1 = Label(
    main, text="&", bg="black", fg="white", font=("Helvetica", 23, "bold", "italic")
)
lable2 = Label(
    main, text="DARE", bg="black", fg="red", font=("Helvetica", 23, "bold", "italic")
)
lable0.place(x=99, y=600)
lable1.place(x=530, y=600)
lable2.place(x=650, y=600)
# *****************************************


# COMBOBOX*******************************
lable3 = Label(
    main, text="How Many Players :", bg="black", fg="white", font=("Helvetica", 10)
)
lable3.place(x=300, y=830)
option = []
for i in range(2, 101):
    option.append(i)
combobox = ttk.Combobox(main, values=option)
combobox["state"] = "readonly"
main.option_add("*TCombobox*Listbox*Background", "black")
main.option_add("*TCombobox*Listbox*foreground", "white")
combobox.pack()
combobox.place(x=280, y=920)
# *****************************************


# MAIN FUNCTION***************************


def main_function():
    try:
        i = int(combobox.get())
        lable3.config(text="Enter Players Name :")
        lable3.place(x=300, y=830)
        players_list = [""] * i
        combobox.destroy()
        input = Entry(main)
        input.pack()
        input.place(x=290, y=920)
        lable4.config(
            text="\nnote:-\ndo not include any special characters\nexcept(_)(underscore) or any numbers in the name\nor it will be removed..\n".title()
        )
        lable4.place(x=0, y=0)

        # ZERO FUNCTION***********************
        def function0():
            x = input.get()
            x = re.sub(r"[0-9]", "", x)
            x = re.sub(r"[^\w]", "", x)
            x = (" ".join(x.split())).title()
            players_list.append(x)
            players_list.remove("")
            input.delete(0, END)
            if "" not in players_list:
                lable3.destroy()
                Output1.pack()
                scroll.pack(fill=X)
                scroll.config(command=Output1.xview)
                Output1.insert(
                    END,
                    "TOTAL PLAYERS : "
                    + str(i)
                    + "\nPLAYERS NAME : "
                    + ",".join(players_list),
                )
                # *****************************************

                # FIRST FUNCTION***************************
                def function1():
                    button0.config(state=DISABLED)
                    while True:
                        get_chance = ["TOP", "BOTTOM"]
                        global chance, chance1, choose, choose1
                        choose0 = random.choice(players_list)
                        chance0 = random.choice(get_chance)
                        choose1 = random.choice(players_list)
                        chance1 = random.choice(get_chance)
                        if choose0 == choose1 or chance0 == chance1:
                            button0.config(state=NORMAL)
                            Output0.delete("1.0", "end")
                            Output0.insert(END, "Spin Again..")
                            break
                        else:
                            Output0.delete("1.0", "end")
                            Output0.insert(
                                END,
                                choose0
                                + " Got "
                                + chance0
                                + " & "
                                + choose1
                                + " Got "
                                + chance1
                                + "\n",
                            )
                            if chance0 == "BOTTOM":
                                Output0.insert(
                                    END,
                                    "\nIt's "
                                    + choose0
                                    + " Chance To Ask TRUTH\nOr Give DARE To "
                                    + choose1
                                    + "\n\n"
                                    + choose0
                                    + " Which One Will You Give ?\nTRUTH (t) Or DARE (d)",
                                )
                            if chance1 == "BOTTOM":
                                Output0.insert(
                                    END,
                                    "\nIt's "
                                    + choose1
                                    + " Chance To Ask TRUTH\nOr Give DARE To "
                                    + choose0
                                    + "\n\n"
                                    + choose1
                                    + " Which One Will You Give ?\nTRUTH (t) Or DARE (d)",
                                )
                            break
                    # *****************************************

                    # SECOND (TRUTH) FUNCTION*****************
                    def truth():
                        Output0.delete("1.0", "end")
                        Output0.insert(END, "TRY ASKING BELOW..\n\n")
                        while True:
                            truthq0 = random.choice(truth_questions)
                            truthq1 = random.choice(truth_questions)
                            truthq2 = random.choice(truth_questions)
                            truthq3 = random.choice(truth_questions)
                            truthq4 = random.choice(truth_questions)
                            if truthq0 == truthq1 or truthq2 or truthq3 or truthq4:
                                Output0.insert(END, "#1 " + truthq0 + " \n")
                            if truthq1 == truthq0 or truthq2 or truthq3 or truthq4:
                                Output0.insert(END, "#2 " + truthq1 + " \n")
                            if truthq2 == truthq0 or truthq1 or truthq3 or truthq4:
                                Output0.insert(END, "#3 " + truthq2 + " \n")
                            if truthq3 == truthq0 or truthq1 or truthq2 or truthq4:
                                Output0.insert(END, "#4 " + truthq3 + " \n")
                            if truthq4 == truthq0 or truthq1 or truthq2 or truthq3:
                                Output0.insert(END, "#5 " + truthq4 + " \n")
                                break

                    # *****************************************

                    # THIRD (DARE) FUNCTION********************
                    def dare():
                        Output0.delete("1.0", "end")
                        Output0.insert(END, "TRY GIVING BELOW..\n\n")
                        while True:
                            dareq0 = random.choice(dare_question)
                            dareq1 = random.choice(dare_question)
                            dareq2 = random.choice(dare_question)
                            dareq3 = random.choice(dare_question)
                            dareq4 = random.choice(dare_question)
                            if dareq0 == dareq1 or dareq2 or dareq3 or dareq4:
                                Output0.insert(END, "#1 " + dareq0 + " \n")
                            if dareq1 == dareq0 or dareq2 or dareq3 or dareq4:
                                Output0.insert(END, "#2 " + dareq1 + " \n")
                            if dareq2 == dareq0 or dareq1 or dareq3 or dareq4:
                                Output0.insert(END, "#3 " + dareq2 + " \n")
                            if dareq3 == dareq0 or dareq1 or dareq2 or dareq4:
                                Output0.insert(END, "#4 " + dareq3 + " \n")
                            if dareq4 == dareq0 or dareq1 or dareq2 or dareq3:
                                Output0.insert(END, "#5 " + dareq4 + " \n")
                                break

                    # *****************************************

                    # FOURTH FUNCTION************************
                    def function2():
                        if cbv0.get() == 1:
                            truth()
                            button0.config(state=NORMAL)
                            checkbutton0["state"] = DISABLED
                            checkbutton1["state"] = DISABLED
                        elif cbv1.get() == 1:
                            dare()
                            button0.config(state=NORMAL)
                            checkbutton0["state"] = DISABLED
                            checkbutton1["state"] = DISABLED

                    cbv0 = IntVar()
                    cbv1 = IntVar()
                    checkbutton0 = Checkbutton(
                        main,
                        text="TRUTH",
                        variable=cbv0,
                        onvalue=True,
                        offvalue=False,
                        command=function2,
                        bg="black",
                        fg="green",
                    )
                    checkbutton0.pack()
                    checkbutton0.place(x=199, y=900)
                    checkbutton1 = Checkbutton(
                        main,
                        text="DARE",
                        variable=cbv1,
                        onvalue=True,
                        offvalue=False,
                        command=function2,
                        bg="black",
                        fg="red",
                    )
                    checkbutton1.pack()
                    checkbutton1.place(x=699, y=900)
                    if choose0 == choose1 or chance0 == chance1:
                        checkbutton0.config(state=DISABLED)
                        checkbutton1.config(state=DISABLED)

                # *****************************************

                button0.config(text="SPIN", command=function1)
                Output0.place(x=-1, y=1500)
                input.destroy()
                lable4.config(text="")

        button0.config(command=function0)
        button0.place(x=440, y=1100)
    except ValueError:
        lable4.config(text="Above Field Cannot Be Empty...")
        lable4.place(x=250, y=1030)


# *****************************************


# BUTTONS,TEXT,LABEL WIDGETS**************
button0 = Button(
    main, text="NEXT", bg="black", fg="white", bd=10, command=main_function
)
button0.pack()
button0.place(x=440, y=1100)
lable4 = Label(main, text="", bg="black", fg="white")
lable4.pack()
Output0 = Text(main, wrap=NONE, height=10, width=44, bg="black", fg="white")
scroll = Scrollbar(main, bg="black", orient="horizontal")
Output1 = Text(
    main, wrap=NONE, xsc=scroll.set, height=2, width=44, bg="black", fg="white"
)
Output0.bind("<Key>", lambda a: "break")
Output1.bind("<Key>", lambda a: "break")
mainloop()
# ****************************************
