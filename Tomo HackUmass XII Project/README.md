# Tomo AI-Space-Invaders
##Inspiration
These days AI is an ever-growing part of our everyday lives. It is only natural that we find a way to integrate this near-limitless technology into our favorite hobbies. Tomo does just this, it integrates artificial intelligence into a game similar to the classic Space Invaders (from whose creator Tomo gets its name). On top of this, due to the generous technology provided by Hack UMass, we were able to implement hand-tracking controls for an even more futuristic feel.

##What it does
Tomo runs just like Space Invaders... at first. With periodic boss fights and constant changes thanks to AI integration each round of Tomo is completely unique and surprising. Some of the things you can expect to see are power-ups like shields or obstacles like portals and black holes! All this combined with the Leap Motion hand-tracking controller makes for a retro, but still immersive gaming experience that will keep you on your toes.

##How we built it
Tomo's main gaming functions were coded in Python using the pygames package. For the AI integration, we used the OpenAI API Platform. We ran a master prompt laying ground rules and expectations for the AI implementation of functions that would alter the gameplay experience of the user. To integrate the Leap Motion sensor we run intake through a C++ script which is piped to the main Tomo program as keyboard inputs. Throughout this whole process, we used VS Code to bring this project to life and GitHub to keep us organized

##Challenges we ran into
The implementation of the AI and training of the AI was definitely our hardest challenge especially converting the responses into executable Python code.

##Accomplishments that we're proud of
We are all so proud of the overall quality of the project in the end game and how we were able to learn and implement tools which we were all unfamiliar with.

##What we learned
We learned so much not just about Python and AI usage, but the entire innovation process. This came in the form of brainstorming ideas, delegating the work, and finally how to innovate under pressure.

##What's next for Tomo?
While Tomo is currently built to be similar to Space Invaders, due to the modular coding structure we used, Tomo could very soon be ready to be implemented in the backend of entire libraries of video games.
