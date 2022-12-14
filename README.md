# Find.it #
Find.it is our submission for the UMASS Fall 2022 Hackathon. Find.it a scalable solution for people who've lost their things and (unsurprisingly) want to find them. 

## Inspiration ##
  Our very initial motive comes from a team member from this group that he wanted to find his stolen bike, a very precious gift, desperately. He encouraged everyone in the team to work on a lost or found project to prevent other people like him to get another item lost on campus. Our main motive for creating Find.it was specifically to address an ubiquitous issue that we saw happen around campus: people tend to lose things quite often. It was sentimental to see students lose things and literally *post flyers on poles* to let others know to look for it. Not only that but there's even *individual* lost and found systems that each dining hall has! None of it is centralized--and that makes it horrifically difficult for people to find their things. That's why we thought that it'd be a good idea to centralize and expedite the process of finding lost things, with Find.it. We realized the items are not always tied to monetary value, but more about special meaning of the items that people cherished. 
  
## What does it does ##
  Find.it is a responsible website that uses a SQL database to store and show data that users input themselves. In particular, this data involves user data (the thing that helps us identify who they are, like their email, name, etc.), and data about their lost item (things like pictures, a brief description, the last known location, and so on). 
  
## How we built it ##
  We built the website using a combination of CSS, Javascipt, and React. Our plan for front-end development was to make the website as interactable and intuitive as possible, since we wouldn't want people who're looking for their lost item to have trouble accessing the site or operating it. So, what we decided to do was make the whole website look like any other website that you would typically see nowadays, since familiarity and accessibility is key! Oh--and one last append: we also used Twilio to help notify the user that their item has been found.
  
  Now as for the back-end, we used MySQL to create the server for the SQL database and from there we made a whole bunch of tables--one for the user name, which is then connected to 2 separate tables where 1 represents lost items, and the other represents found items. Then *those* are connected to another table that details information about the (technical parts) of the item itself, like the id of that item in the system, their written description, and so on. Finally, *that* table is connected to one last table that categorizes the item. Talk about a mouthful!
  
  Personally, as the guy who's writing this, I wish we did go to workshops to learn more about web design and the like, but there's also nothing better than discovering how to do these things by ourselves. It's the struggles that help us figure out the right path forward.
  
## Challenges we ran into ##
- ALL OF US has an very minimum experience with React and Flask, so we have had to learn it from scartch starting this Friday!!!
- A challenge that we ran into in particular was actually designing the website--the minute details like figuring out why our little magnifying glass icon started reshaping itself and flying off to the other side of the screen when we shrank the window for the website. Or, figuring out why someone completely missed how to spell the phrase "sign up" and instead just wrote "sign". Figuring out how to work well as a team was honestly one of the bigger struggles that we hate to admit. It's hard to coordinate and communicate when a majority of the team is in person, save at least one of us who was completely remote. That one guy had a bit of trouble getting everyone to answer his questions promptly. ~~That was the guy writing this description~~. So, with these difficulties, you can imagine some of the difficulties that have to do with choosing the direction for the site in terms of visual design, mechanics, and the like. 

## Accomplishments we're proud of ##
  - Honestly, we're just proud that we managed to get a functioning website with a functioning database and managed to put a huge chunk of it into motion in less than 24 hours! Obviously it didn't come easy, but the fact that *we did that* is just astonishing. 
  - Finished the project on time
  - Able to learn new technology in a limited time 
    - website framework, database configuration, and integration between front and back end
  - learned how Git works
    - effectively manage the project by creating multiple branches, merging, and making pull request -- two notable ones are "git add ." and "git commit -m "project completed"

## What we've learned ##
  - Of the people who worked on this project, I'm (the writer) am almost 100% certain that everyone learned at least one new thing while working on this project: creating endpoints for the front and back end. You know, so they can work together as a functional website and not just 2 separate entities that *seem* to look nice together? Yeah--anyway--most of us in the front end really got to know how to use React. In fact, the whole reason why half of the team chose to do front end development was because that was something that they had little to no experience doing! The front end team really wanted to understand how to use industry tools like React to help not just themselves but everyone around them in the future. As for back end, some of us (much to our chagrin), had to figure out how to use Python and Flask, and even SQL just to get the website a proper back end. The amount of the work we have on database configuration and making efficient database schema to make the queries faster is a lot.
  -  A few of us has experience with software engineering experience, and we are able to treat it like a project that we got assigned to in an actual real world setting such as an internship 
  - Communication is the key. There were times that we have difficulties understand the terminology we used. Communicating effectively to make sure each part of the project is well designed. 

## What's next for our hack ##
  - Our vision for this hack, if the whole team decides to make it large scale, would be to seriously start making things work. We could keep the website as is, or make it just a tad bit better (blanking on ideas at the moment, bare with me!), and potentially make an app for iOS and Android so it's even more accessible! Our initial idea was to just make it easier for people to find their things, so naturally the easier we make things, the better it'll be. The endeavor itself was already a huge one and the fact that we even did *anything* about it is a milestone in and of itself. It was definitely a learning opportunity for most of us (some of us, the writer included, didn't even know how to *make* a website). As for future hackathons, we're not too sure! We'll definitely take this experience along with us when we decide to finally go after a new hackathon!
  - We will seriously add more components, and deploy the website using AWS before June 2023.
