MCP Security Working Group

# Metadata

 **Title:** MCP Security Working Group
**Location:** Zoom
**Date:** 2026\-01\-07T18:00:32Z UTC
**Attendees:** HilsChan, Kurt Seifried, Colin Lowenberg's Workspace Sembly Agent, Mary Becken, Rajath Ravikumar, MatthewHoerig, Colin Lowenberg, Zenith Law, Robert de Monts
**Link:** [https://app.meetgeek.ai/meeting/e4fffa15\-997e\-4bf6\-a0a9\-2e35c323d89e](https://app.meetgeek.ai/meeting/e4fffa15-997e-4bf6-a0a9-2e35c323d89e) **Agenda:**
30\-Minute General Meeting AgendaOpening and Welcome (1 minute)Quick welcome and introduction to the meeting's objectives.Review of Action Items (3 minutes)Brief update on the status of action items from the previous meeting.Key Discussions (20 minutes)Focused discussion on one or two key issues that need input or decision\-making.Time\-bound to ensure brevity and relevance.Next Steps (3 minutes)Quick summary of action items arising from the meeting's discussions.Assigning of responsibilities for these items.Wrap\-Up (3 minutes)Final thoughts or comments.Confirm the time for the next meeting.

# MeetGeek Transcript

 **Unknown speaker \- 00:09**Thank
you.
So yeah, I'll just give people, like I said, about till five past.
Okay, uh, I guess, well, we'll give people one more minute.
Let's see everyone.
So today we'll be focusing on the MCP Marketplace security report.
And I just put the various things we're looking at checking with AI tools and some other tools, like classic DNS lookups or HTTP headers, that kind of stuff.
 **Unknown speaker \- 02:51**Okay, so I guess we'll get started.
So this is the MC, oh, let me turn on recording.
Sorry.
This meeting is being recorded.
There we go.
Okay.
Excuse me.
 **Unknown speaker \- 03:02**All right.
So yeah, this is the MCP security technical group meeting.
And so basically what we're doing is a lot of your MCP servers, obviously, you got your MCP servers, obviously.
You have your MCP clients that use the servers.
You have your MCP clients that use the servers.
And the MCP marketplace is because, well, that's how people get their MCP service, right.
And so what we're looking at doing is essentially security research into all the major MCP marketplaces and the MCP clients.
 **Unknown speaker \- 03:53**And for example, on the marketplace side, ah, speak of the devil.
Your ears must be burning call on.
So we're looking at the marketplaces, you know, and things like, do they accept security reports?
You know, will they take down a malicious MCP server?
And then we'll also be looking at the MCP clients and things like, do they give administrative control over what stuff people do and do not do with them, or, you know, install the servers and stuff.
So today I was hoping to go over the, essentially the security checks.
We're looking up for the MCP security marketplaces to make sure we're not missing anything because, you know, like everybody, I have blind spots.
 **Unknown speaker \- 04:38**So I'll just put that link in chat again.
And let me just share my screen.
Do do do.
Share Google Chrome.
So yeah.
This is the MCP marketplace get repository.
In general, we use Obsidian note\-taker format.
 **Unknown speaker \- 04:59**So there's YAML metadata up front.
That's this kind of wonky table looking thing.
So looking at this at a high level.
We're basically looking at a couple of categories for the MCP marketplace.
So things like identity and ownership.
Like who actually owns and controls this thing.
For some people, for some people, you know, they're not allowed to use stuff from certain countries.
 **Unknown speaker \- 05:29**We also looked in at what capabilities does this marketplace offer?
Because some are just a website and some like Smithry are a fully integrated command line thing.
We look at what it integrates with, like which clients, the infrastructure they have, you know, their endpoints, so they provide APIs or anything.
Then we do content and analysis.
So like actually looking at their website or whatever and trying to figure out what it is they're doing.
Do they have contact information?
Some don't.
 **Unknown speaker \- 06:01**Do they have like a security reporting mechanism?
What is their supply chain?
What are they hosted on?
And then anything, do they have a privacy policy?
Fun fact, many don't.
And especially if they have no privacy policy, that, you know, that's a bit of a red flag.
And then, because we can, searching for external discussion of them, like on hacker news, reddit, right?
 **Unknown speaker \- 06:28**Because that's the thing we can easily do now is you can ask the AI like, hey, can you search for chatter about this MCP marketplace for like the last week or two.
So with this in mind is there any kind of concerns or like what do you, when you are looking at an MCP marketplace, what are your concerns or what are the things you're worried about?
If anybody, even if things we've covered, I also want to make sure that we kind of fully understand them.
So if anybody has any thoughts or comments on that, please, well, raise your hand or just start talking, I guess.
 **Mary Becken \- 07:06**For me, I'm thinking about versions and updates like we've seen with MPM lately on
 **Kurt Seifried \- 07:14**some of the themes.
Versions, how the hell did I miss that?
That's a good point because, hmm, yes, okay, yeah, versions and updates.
So for example, well, one thing that comes to mind is like, if you download the MCP server, is there some mechanism to tell us something that you really, really need to update it, things like that I'm assuming.
 **Mary Becken \- 07:31**Right, and just... See, I have blind spots.
Holy
 **Kurt Seifried \- 07:33**crap, how did I miss that?
I'm
 **Mary Becken \- 07:36**scarred for life by the NPM thing.
Sorry, I didn't
 **Kurt Seifried \- 07:39**catch that.
I'm scarred for life by
 **Mary Becken \- 07:42**the NPM incident.
Yeah, well, I mean, it's funny
 **Kurt Seifried \- 07:45**because I've spent, you know, seven years at Red Hat on the product security team, like, really caring about updates of software and versioning and like, yeah.
What about versioning and updates and like notifications of problems.
Because the other thing that comes to mind too.
My favorite thing is, I have that zoom thing enabled where it like intelligently does my camera.
So let me just turn that off.
That is horrible.
Auto frame.
 **Kurt Seifried \- 08:18**Yeah, no, don't want that.
But like every time, you know, NPMJS or whatever, some developer can't gets hacked, and somebody replaces their stuff with malicious code.
And it's kind of like, you know, we think we sort of told everybody publicly, but I think we all know that there's people that just, you know, they're busy, they don't pay attention, they deployed it, they forgot about it.
 **Mary Becken \- 08:40**Yeah, or they don't care because... Well, yeah,
 **Kurt Seifried \- 08:43**exactly.
That's my deal.
Like, I actually bought some link sys access points.
that I thought they had to find out then that they hadn't received any updates in like two years because the links has basically abandoned the product.
Like,
 **Mary Becken \- 09:01**thanks.
So yeah,
 **Kurt Seifried \- 09:04**that was a fun, yeah.
So versioning and updates and notifications of problems or need to stop using that MCP server.
Yeah.
Because, okay, Matt.
Sorry, I'm Matthew.
I shouldn't shorten your name.
No, I'm just
 **MatthewHoerig \- 09:25**calling Matt.
Okay.
It's okay, Kurt.
So quick question.
The last time you spoke, I think I told you that I'm embedded with the federal government here in Ottawa.
For a lot of the AI activities and initiatives taking place at the government, the department and agency level.
One of the things, of course, that is a super, sign is the idea of service authorization, right.
 **MatthewHoerig \- 09:54**And so
 **Kurt Seifried \- 09:55**when you look at that, you know, you know, you
 **MatthewHoerig \- 09:57**mentioned before the idea of ensuring that the MCP marketplace is available.
Either reports or some kind of indication in terms those data sources could be, could be risky or something that allows us to better evaluate what the risk of that is.
If I look at the federal government right now, we're going through the process of developing AI marketplace, like an AI marketplace for both models and apps built on top of, think on infrastructure.
So the idea is that if we stand excuse me, if we stand up, a model, some, some data source.
We just want to make sure that is a trusted source and that there's some, some indication, what that potential risk level might be, know.
Yeah,
 **Kurt Seifried \- 11:00**so for the actual MCP server kind of security side of things.
I'm kind of punting on that for a few weeks.
Because, well, to put it bluntly, we can't do a comprehensive report on MCP server security, because there's like 20,000 of them,
 **MatthewHoerig \- 11:12**right?
Understood.
Whereas the marketplace is it's manageable
 **Kurt Seifried \- 11:15**at about 100 and the clients at about 100\. And also, those are very much, I think, blind spots for a lot of people.
Now, with respect to the MCP, server security, we absolutely, here.
Well, let me just show instead of tell.
We absolutely are going, well, we are covering that.
And so for example, where is So the first thing, oh, sorry, let me just meet, view all repositories.
Where is it?
I'm blanking out.
 **Kurt Seifried \- 11:53**Okay, yeah.
So from the MCP server point of view, there's sort of three main things we do.
Number one is we're looking at an MCP server finder.
And so that is like actual prompts and tools to help you find, not just like a secure MCP server server, but, oh, perfect example.
There are a Kajillian WordPress MCP servers.
So which ones actually have like coverage of the features that you need, right.
So a good example is Tableau.
 **Kurt Seifried \- 12:22**Tableau has a really good MCP server that only does like data level stuff.
It doesn't do any administrative functions.
So from like a user's point of view of I want to use Tableau.
It's perfect.
From an administrator's perspective, it's useless.
It's like, it can't add a user.
And well, that's, kind of how they scoped it.
 **Kurt Seifried \- 12:42**So that's like a wordpress plug\-in that like can't interact with pages.
And I'm like, well, that's, I don't want that, right.
And then the finder also obviously cares a little bit about security to a degree of like kind of the public signals that we can find.
And then the next one is the MCP is the next one.
And then so that would be where the things like doing a data flow diagram.
Okay, it's sending data over to this
 **MatthewHoerig \- 13:16**thing.
We should maybe figure out
 **Kurt Seifried \- 13:18**where that is.
Oh, it's in like China or it's in Tajikistan.
Okay, that might be a problem for Or maybe not.
 **MatthewHoerig \- 13:26**And then the right thing.
Like an
 **Mary Becken \- 13:29**MCP bill of material.
 **Kurt Seifried \- 13:32**Well, well, yeah, because, and that's actually a good point.
I've been thinking about S\-bomb, you know, software bill of materials.
And I think we kind of need to expand the concept of S\-bomb to include data flow, because in the AI world, data is also executable content.
Like, it is instructions, or, you know, it's what we act upon.
But um, so the idea with MCP server audit is that you would audit an MCP server or multiple servers and find one that's good.
And also with in conjunction with the MCP server builder, fix it maybe, right.
And then also maybe you submit the results to our audit database, which then has the advantage of, obviously, we start to build that public knowledge of like, what flaws are people finding, like, which ones are more common and less common, right?
 **Kurt Seifried \- 14:21**So how does that
 **MatthewHoerig \- 14:22**work, or is that like, if you select that, does that trigger some kind of like VA or something, or like, how do you establish a baseline in terms of what the state of the server is?
 **Kurt Seifried \- 14:34**Sorry, what do you mean, like... In other
 **MatthewHoerig \- 14:37**words, when you select the MCP server audit option here, like... Yeah,
 **Kurt Seifried \- 14:41**it's just, there's like prompts and stuff for example.
Like you would use the prompts to and run them against... code, and we've already got like a bunch of security checks that we figured out, but obviously there's going to be more.
Okay, so it
 **MatthewHoerig \- 14:51**doesn't, it doesn't address anything in the underlying infrastructure.
It's just... It
 **Kurt Seifried \- 14:56**could, I mean, we could definitely add that, and probably should, because that's
 **MatthewHoerig \- 15:01**part of the whole, like, you can't just like... Yeah, agreed, agreed.
Like, your doctor
 **Kurt Seifried \- 15:05**doesn't just look at your heart, and he also looks at your stomach, right?
Yeah,
 **MatthewHoerig \- 15:08**yeah, yeah.
But, and see, that's part of the
 **Kurt Seifried \- 15:10**magic of this is... We can take what you know, we can take what you just said and add that as a high level goal to the tool and then have the AI, you know, kind of redo all the prompts and redo the specification and redo the project plan in a way that, you know, like as humans, it would take us a
week, whereas with the AI, we set that, like, hey, instead of just auditing the code, let's also think about auditing all the way down to a reasonable level of abstraction, like
 **MatthewHoerig \- 15:34**the underlying, oh, they're using AWS, okay, you know, obviously
 **Kurt Seifried \- 15:38**we're not going to audit AWS, that's out of scope, but
 **MatthewHoerig \- 15:41**what are you using on AWS and Are
 **Kurt Seifried \- 15:43**you're using an S3 bucket?
Okay, you better make sure it's locked down or else you're gonna have a bad time.
Yeah,
 **MatthewHoerig \- 15:51**right.
That makes sense, make sense.
And then
 **Kurt Seifried \- 15:54**also one thing that I found early on is the MCP server kind of hosting.
So where is that, hosting here?
So perfect example.
I have run MCP servers in Docker containers, which thank God I did because early on, was like Cloud 4 was designed to be very helpful.
So a perfect example.
I was writing a doctor or I was writing a Python program that did some stuff.
Then I wanted it to be in a doctor container so I could, you know, use it and run And I asked Claude to write some tests to make sure that everything worked.
 **Kurt Seifried \- 16:34**And Claude wrote the test, and then it very helpfully tried to execute them.
And it had file system access in a Docker container.
And so it could read and write files, but it couldn't run anything.
So it basically tried very, very hard to like run stuff and said, I can't run stuff.
I have access to a web container that can run JavaScript.
I can execute it through there.
And luckily it was in a separate container so that it actually went into that container.
 **Kurt Seifried \- 16:57**It was like looking for the files and trying to run them and like couldn't find the files.
And it was very apologetic.
But it like literally was like a cat running out the door.
Like it was trying its damnedest to escape.
not like, I really want to run these tests and make sure that they work.
And I'm like, please, like, that's my job.
Let me do that.
 **Kurt Seifried \- 17:14**And so part of it is there are safer and obviously less safe ways to run and host MCP servers.
And so for some people, like, hey, run it on your laptop.
Okay.
And for some organizations, you know, they're going to want to centralize it and lock it down and have centralized logging and You know, like, I've already had the experience of having to troubleshoot people's MCP, client and servers.
And when they're running it on their laptop, it's like, well, it's kind of a chore.
Whereas if it was like centrally run, we would have immediately noticed that they had an expired API key, right?
And it would have been a 10\-second fix.
 **Kurt Seifried \- 17:51**But because it was on their laptop, we had to kerfuffle about with screen sharing and back and forth, and it took like 20 minutes.
That would
 **Mary Becken \- 17:59**be a good thing to add too, different ways it has to be local or remote.
 **Kurt Seifried \- 18:06**And what are the differences between two?
I know the GitHub one is
 **Mary Becken \- 18:10**very different depending on how you Well, and
 **Kurt Seifried \- 18:12**then, and actually this speaks to the MCP marketplace is there's a, I think we have a total of 14 different kinds of MCP marketplace, like everything from like there's a website with links, good luck to, you know, like the Microsoft fully integrated store model that's going to be coming to Windows
or the, um, There are, well, like cloud desktop.
It's integrated into the tool.
 **Mary Becken \- 18:36**There's other ones where they have an
 **Kurt Seifried \- 18:39**MCP marketplace and then they run it for you because like, it's kind of easier.
And so yeah, those are absolutely, I mean, concerns.
And luckily, we've already addressed a lot of this with cloud computing, running your stuff on somebody else's machine.
 **Mary Becken \- 18:54**It's a very common problem.
 **Kurt Seifried \- 18:57**And so that's sort of the four main components, right, finding them, I don't see, I'm spacing out.
I'm spacing out.
I'm spacing out.
Yeah, so MCP server, finder, end, and then, you know, I'm spacing out.
Yeah, so MCP server, finder, audit and builder, operator, and then... And then also the hosting of it.
And again, like as a, as a, as a person.
There's obviously more and less secure things you can do, right?
 **Kurt Seifried \- 19:36**So does that kind of answer your question around the MCP server security stuff that we're looking at longer term?
Yes,
 **MatthewHoerig \- 19:42**sir.
Thanks, Matt.
And... If
 **Kurt Seifried \- 19:45**you can think of this too is like, this is only 14 months, well, not even.
It's 13 and a half months old at this point.
You know what I mean?
And we're
 **MatthewHoerig \- 19:54**constantly reinventing it.
Like,
 **Kurt Seifried \- 19:57**you know, things change.
Like a good example is the CWE that talks about prompt injection was written a year and a half ago, and it only talks about the system prompt.
And I'm like, well, that's completely wrong and obsolete nowadays.
 **MatthewHoerig \- 20:13**But, but, okay, so
 **Kurt Seifried \- 20:16**yeah, the versioning updates, essentially having some sort of, is there a communication channel to inform you that like, hey, look, there's a problem.
And it comes to mind also that you were logged into the marketplace, so they have your email address and they could email you saying, hey, you're using this thing that's bad, don't or panic or whatever.
But it also occurs to me that, from, and we've seen this in a lot software where the software will explicitly, like every time it starts out.
It connects to an API server to say, like, what's the latest version?
And like, I am this version, how critical is it that I update or am updated.
And then maybe it tells the user.
Or I've seen even in some cases where if the software gets too out of date, it will then refuse to run and be like, look, you absolutely have to upgrade me because I'm like, dangerous.
 **Kurt Seifried \- 21:07**Now, I'm full of security flaws, right?
 **Mary Becken \- 21:09**Obviously, this is rare, but That
 **Kurt Seifried \- 21:11**could be a good danger point
 **Mary Becken \- 21:14**though, too, if I was trying to hack one.
Oh, yeah, absolutely.
It's
 **Kurt Seifried \- 21:17**a huge privacy nightmare.
Yeah.
And it's always these trade\-offs, right?
 **Mary Becken \- 21:23**Right.
But I think that's something
 **Kurt Seifried \- 21:26**we need to think about, because I have a feeling.
Most people install software and set it and forget it.
Like the Ronco rotisserie, if you're old enough to remember those little things.
And I feel like, especially MCP servers, like, if it works, people are going to ignore the heck out of
 **Mary Becken \- 21:43**And they're just going to use you know.
 **Kurt Seifried \- 21:48**So, okay, so the AI came up with some obvious things like, obviously, versioning, you know, and that's a good example too.
Like, anything with an update mechanism is by definition arbitrary code execution because it might be not malicious today, but if it doesn't update and installs whatever the heck they gave you, right?
Who knows what it's doing?
And so that's a good example of where some people might be like, it has to have update capabilities.
And some people will be like, we have to block that or we can't allow that.
That's not allowed, right?
In client warnings.
 **Kurt Seifried \- 22:25**That's a good point, actually.
Something for us to think about is, this isn't like dumb software.
This is a tool that could like talk to the user and say like, I am really out of date.
I am dangerous.
 **Mary Becken \- 22:40**And the user is like, no, and the user's like, no,
 **Kurt Seifried \- 22:42**perfect example.
Oh, perfect example.
Red Hat has some concepts on how people are supposed to use Red Hat Linux.
So one example is that the root user should be able to shut down the machine.
Now the NSA, who gave us SE Linux, security\-enhanced Linux, actually has the ability to take away that capability from the system.
And so every time there's like a Linux kernel like denial of service or panic or something.
The NSA would be like, you have to fix this, this is critical.
 **Kurt Seifried \- 23:15**And we'd be like, no, like the root user can shut down the system.
That's just how it works.
And the NSA is like, no, that's not how we view the world, right?
Or another view of it was Red Hat had a view if you use like NFS or SMB or CIFS file sharing, That has to be restricted to be trusted local networks and clients.
You cannot expose it to the internet.
And of course, there are people that do.
And they're like, I need my security fix now.
 **Kurt Seifried \- 23:40**And Red Hat was always like, you're insane.
Please, for the love of God, lock that down.
And so that's part of that is the AI can understand this risk profile and maybe can say like, hey, I have this security issue.
Oh, but you're using me with an internal trusted server.
OK, that's probably safe.
We'll carry on, right?
deprecation and end of life.
 **Kurt Seifried \- 24:01**That's a good one too, because I've noticed a lot of these MCP servers.
People have a tendency to write them and then like abandon them because they work and they never update it, right?
And again, that might be okay or not okay.
So, okay, so that's a good one.
Yeah, versioning and sort communication channels around usage.
As far as far as far as far as far,
 **Mary Becken \- 24:37**I was just thinking, wonder if people would pay for a service that kept in very secure repository of MCP servers that they tested all the time.
mean, not
 **Kurt Seifried \- 24:52**yet.
Yeah, not that I'm trying market
 **Mary Becken \- 24:55**anything at all.
I'm just thinking, I'm just thinking what would be is something that's
 **Kurt Seifried \- 25:01**already pre\-tested.
Yeah.
So, well, that's a good example is it would be, like at the Cloud Security Alliance, we primarily use chat GPT, cloud and Gemini, right, the big three, right?
 **Mary Becken \- 25:14**And so for example, with
 **Kurt Seifried \- 25:16**Cloud Desktop, sorry, my cat's being goofy.
With Cloud Desktop, it's really simple.
If Cloud Desktop ships an MCP server internally, you can use Like, we try to have hopefully be audited or made sure that these things are not malicious.
And so you can just use whichever ones are there.
And you know, we use the air table, the Google stuff, you know, all that sharepoint stuff quite heavily.
Same thing with like, well, with chat GPT, you know, it's there's more of a marketplace.
And honestly, I'm just sort I'm in a lucky position where most of what the CSA does is public, like I'm not a bank, we're not healthcare.
 **Kurt Seifried \- 25:52**So I can sort we let the users a lot less risk for us.
And obviously that's not going to work for a bank, right.
And that speaks to the MCP client security report and paper we want to do, which is like, which of these will actually allow you to have some control over what the heck your users are doing.
And some of them, you could kind of fudge that control by saying like, okay, we're going to like lock, like on Windows, for example, we're going to lock down that dot cloud path of course, and like, you know, set them to be statically, only allowed these certain MCP servers or whatever.
And some clients really don't even give you that capability, for example.
 **Mary Becken \- 26:35**So, you know, and that's the thing.
Like... So many ways around it, too?
 **Kurt Seifried \- 26:39**Yeah.
And a great example would be too, like, well, Quad Desktop allows you to also put in URL to, like an MCP.
Some of them allow you to just, you know, here's a hosted MCP server.
Go forth and like, use it.
And for example, do any of them allow for block listing or allow listing of whatever the heck people are connecting to.
 **Mary Becken \- 27:07**Right.
And the
 **Kurt Seifried \- 27:10**answer is like, as far as I know, none yet.
I mean, it'll probably happen, but
 **Mary Becken \- 27:14**I think it will.
I mean, I can see some like DNS redirection things happening possibly.
That won't
 **Kurt Seifried \- 27:21**work.
It's not granular enough.
 **Mary Becken \- 27:23**You know, you know, I think that will.
And that will work.
And that will work.
And that will
 **Kurt Seifried \- 27:30**work.
No, because deep packet inspection essentially is a nation\-state level attack on an HTTPS stream, which all the libraries and clients are effectively blocking.
So it kind of, even the thing where you like install a custom certificate that then signs everything.
 **Mary Becken \- 27:45**Like even stuff like that, Chrome is like, no,
 **Kurt Seifried \- 27:48**not doing And we're going to see that with a lot of these MCP clients where they're going to use whatever HTTPS library securely.
And so the moment, like, the other problem is that deep packet inspection.
It's like, I get that some, like finance.
I think, I want to say SOX.
I think SOX has some clause where you have to be able to see what's on your network,
 **Mary Becken \- 28:14**which, you great, except we encrypted
 **Kurt Seifried \- 28:17**everything 10 years ago.
I
 **Mary Becken \- 28:20**think realistically, to
 **Kurt Seifried \- 28:25**me that is, I understand why people do that.
But to me, I think it would be better to like, instead of trying to staple it on.
It needs to be more built\-in.
And especially if it's like an MCP client, and I care about security, then I need to have one that let's me care about security and doesn't force me to do all this extra silly stuff.
 **Mary Becken \- 28:46**I just don't trust... very easily so.
Well, and we're
 **Kurt Seifried \- 28:51**going to see a hybrid model to some degree, because a perfect example is I have multiple MCP clients on my system, right?
I have chat GPT, I have cloud, I have Gemini, blah, blah.
And it's super annoying because I want to have air table installed for all three of them.
And so the easiest workflow is you install air table using the cloud code command that just installs air table.
And then you have to, then you can actually cut and paste the JSON config into chat GPT or Gemini.
One of them.
But then the other one, chat GPT or Gemini uses, what is Toml configs, Tom's own markup language, which is like some weird bastardized version of YAML.
 **Kurt Seifried \- 29:34**And so I have to like ask the AI to convert it into Toml and then, you know, put that in a different file location.
And so now I have all three working, if I change my API key, I have to go edit it in three spots.
Whereas, with the Windows model, what'll hopefully happen is essentially Windows will have a marketplace.
I will install the AirTable MCP server and it will be like running locally on a port.
And I just pointed at that and I don't have you know, derp around with anything else.
And so I think that hybrid model will become popular because, like, as IT, I care very much about the MCP servers.
I only care about them to not let them not let them do all my MCP and I am, so know, I can have all my MCP clients using those approved MCP servers reliably, then I can stop caring about the MCP clients so much, if that makes sense,
 **Mary Becken \- 30:31**And again, like, I don't know
 **Kurt Seifried \- 30:32**that Windows will give us this capability, but I have to assume that Microsoft is not stupid.
this is the kind of thing enterprises want,
 **Mary Becken \- 30:41**Yeah.
 **Kurt Seifried \- 30:45**But definitely, because, like, part of it is well, and this is something we look for in the Institute marketplace, most of them only cover software that's like available for download.
Like they scan GitHub, they suck it all in.
And they're a virtual credit card provider for expensing and stuff.
 **Mary Becken \- 31:09**And they have a head of course, I'm going to go home go to go to go
 **Kurt Seifried \- 31:12**and see if it doesn't appear in most of the registries.
And so ironically, what is probably the more secure MCP server, which is the vendor\-hosted ones are not most of these registries at Yeah,
 **Mary Becken \- 31:28**And obviously that's
 **Kurt Seifried \- 31:29**going to have to change.
And that's something
 **Mary Becken \- 31:33**to keep in mind.
 **Kurt Seifried \- 31:36**Yeah.
And that's something to keep in mind too.
So this, the idea of the security report is, well, obviously to have a security report and figure out where we are, but also to figure out what's important and to try and help them level up.
So the plan is we're gonna figure out what we want in the security report, and then I'll have the AI basically go do the research and generate them.
And then say, hey, we, you know, we did a security deep dive on you and here's what we found.
Is it correct?
Are we missing anything?
 **Kurt Seifried \- 32:08**Like, do you maybe have a compensating control for potential problem we found or whatever, right?
And give them a chance to respond hopefully maybe fix a few things.
And then, like I said, so part of it is the report of like, you know, which MCP marketplaces are good less good or more suitable for what you want.
But also like, kind of here's what we probably need to start pushing them to do and to be better You know, like a really simple one I feel is gonna be what's, like, NPMJS.org and all have gotten really good at like there's a malicious NPMJS, And as soon as they, they're probably removing it in tens
of minutes, like, less than an hour.
And
 **Mary Becken \- 32:55**you know, and it's like, you
 **Kurt Seifried \- 32:57**know, if I could get anything else in my life fixed that quickly, I'd be so happy.
 **Mary Becken \- 33:04**Well, you know, and that's a good example
 **Kurt Seifried \- 33:06**of like, I've had MCP marketplaces download my mirrored stuff as MCP servers, and I'm Please don't be updated.
never be updated.
Please don't point people don't point people there.
And to date, I've gotten zero responses.
 **Mary Becken \- 33:27**Okay.
So like, I'm sure it's
 **Kurt Seifried \- 33:29**fine.
Yeah, right.
But yeah, so, okay, cool.
As far as then... Like, like, are people here using them, which ones, or I guess a better question to be, why are you using the ones that you use.
Like, for me, it's simple.
I use the cloud desktop one, because it's built in, and I have It's just easier.
But yeah, our other, like, what other marketplaces are people using and why are you using I think would be interesting.
 **Kurt Seifried \- 34:09**Or what tools are people using with MCP servers?
You
 **Mary Becken \- 34:15**know, I'm pretty much security focused.
And right now it's the big push is trying to lock down what our developers can So
 **Kurt Seifried \- 34:23**I'm not sure I've been using any
 **Mary Becken \- 34:28**marketplaces per se.
It's more like just trying to control, trying to catch, trying to prevent that sort of
 **Kurt Seifried \- 34:39**So I'm here with respect to like locking down the developers.
Do you mean like they're installation or configuration of these MCP servers?
Yeah,
 **Mary Becken \- 34:48**and which ones they're using.
And it feels like the Wild West, honestly.
Oh,
 **Kurt Seifried \- 34:54**yeah.
Oh, and that brings up a great example of something I realized a long time ago that I haven't seen addressed in any MCP client, which is, you know, the MCP clients, some will let you restrict or choose which MCP servers you can install.
But I'm like, this end to be to be sure.
I'm like, this end to be sure.
It's a lot to only do the read actions, not the right actions.
Like for a database.
I've not seen that.
 **Kurt Seifried \- 35:22**And obviously, it seems like that's something that we need, you know, because you want to know that your developers use MTV servers, but some of them are We're that thing because the potential for oopsies is way too high.
 **Mary Becken \- 35:37**Yeah.
And if the tools change over a person.
 **Kurt Seifried \- 35:41**Yeah.
I have to be aware of Oh, yeah.
That's a good point.
Oh, that's a good point.
How would we phrase it?
And this isn't for the marketplace so much, but for the MCP server, change logs are nice.
But
 **Mary Becken \- 36:02**yeah.
Having like an AI analysis of the
 **Kurt Seifried \- 36:04**change logs and like what it really means, and especially for you to then say here is my concern.
has this is like, is this a problem in any of these updates, right?
Like, did you add automated updates?
Did you add right capability to this database one, or things like that?
would that maybe be something that we want to...
 **Mary Becken \- 36:27**Yeah, and also even just, if the tool description changes, or even the MCP description changes, that can create some inconsistencies, I guess.
 **Kurt Seifried \- 36:41**You know what would be, okay, so in the MCP servers that are in GitHub, we would be able to look at a previous version and say here was the, I forget what you call it, like the hello message.
You know initially connects and says, hi, I'm an MCP server, I can do this, that, and the other thing, And then obviously the tools that it lists as available, we would be able to suss out from the source code.
But for hosted ones, unless somebody connects and records Like, it's lost to
 **Mary Becken \- 37:16**me as
 **Kurt Seifried \- 37:16**a side project.
We might want to, or we should probably.
 **Mary Becken \- 37:22**Like for the MCP clients, it
 **Kurt Seifried \- 37:23**occurs to me that might be a useful flag to be able to essentially every time you connect to an MCP server.
ess, especially
if it's changed since the last time we got called.
And maybe inform the internet or something.
Because that means something is changed on the remote end.
The other thing I'm seeing is like some, but not all, like they'll say like, I'm an MCP server that does blankety blank.
I'm version 1\.0\. I'm version 1\.1\. You know, and at then you Chanceauly on that.
 **Kurt Seifried \- 37:59**I'm at.
Right.
Yeah,
 **Mary Becken \- 38:03**Sorry,
 **MatthewHoerig \- 38:05**sorry, I wasn't sure if you're asking me.
Okay, quick question for you.
So I wanted to see if I could just, I guess I won't.
I was gonna share my screen with...
 **Kurt Seifried \- 38:18**Oh, sure, I can hear.
Let me stop sharing, then you can share.
Yeah,
 **MatthewHoerig \- 38:23**okay.
Or
 **Kurt Seifried \- 38:25**I might have to give you some sort of permission.
Let
 **MatthewHoerig \- 38:28**me go share.
Yeah, can you guys see this.
Oh, there we
 **Kurt Seifried \- 38:34**Yeah.
Okay, so this is what I wanted to
 **MatthewHoerig \- 38:37**you.
So this is what I wanted to show you.
So I have to be cautious here because this is from a larger diagram for what's called the, it's actually being called the CCAP, which is the Kidian cloud AI
 **Kurt Seifried \- 38:53**platform marketplace, what the official kind ridiculous
 **MatthewHoerig \- 38:56**name is.
But this layer here is a tooling layer.
And so when
 **Kurt Seifried \- 39:00**I look at this and then I look at this
 **MatthewHoerig \- 39:03**other diagram, which is essentially a flow diagram from the MCP client to the server to the, I guess, the source, which in this case, could be some kind of database.
If I extrapolate from that, the MCP client would largely reside, I think in this layer.
Is that
 **Kurt Seifried \- 39:25**So currently, MCP clients tend to be the user interface chunk of the system, like my cloud desktop, my, you know, my Libra chat web interface to an AI, right.
However, I'm seeing is a move to essentially Right now a lot of MCP servers are, I'm going to call them dumb in the sense of they're not dumb, but they're dumb like, I talk to WordPress, that's all Right?
Okay, cool.
You know, that's helpful.
 **MatthewHoerig \- 40:00**But what I'm actively working on, for example,
 **Kurt Seifried \- 40:02**is an MCP server.
that is actually an entire AI and client itself of multiple servers.
So a good example would be right now we have the idea of like, oh, I attach the WordPress MCP server to my client so that I can be like, hey, you know, let's write an article together and then publish it to the WordPress website.
Cool.
But what I actually, I don't want that.
What I want for the sake of argument, is persona editor writer thing that has access to a bunch of databases and the wordpress server image generation and a bunch of other stuff so that I can give it, you know, much more high\-level queries hey, we're gonna publish a wordpress article together.
Here's the outline, let's work on it together, and then, you know, I'll want you to publish, I'll want you to generate images and blah, and it'll encapsulated in MC is a client.
 **Kurt Seifried \- 40:55**And we're going to see more of that.
Because obviously, like me having to tell the thing to publish to WordPress.
What I want is a thing or a better example is I have this publishing thing that will publish to WordPress and to Twitter to GitHub.
So for example, I write a blog entry.
Okay, we'll also construct a tweet and send it out.
We'll also, you know what I mean?
Like it'll do kind that whole workflow encapsulated.
 **Kurt Seifried \- 41:22**And so what we're going to see long term for sure, because it's just too dang valuable, is your MCPD server will almost certainly also be a client, and it'll be turtles all the way
 **MatthewHoerig \- 41:34**And that will
 **Kurt Seifried \- 41:36**generally live at that kind of like the human telling the AI what to do, and then the AI telling more AI what to do.
 **MatthewHoerig \- 41:43**And so, that's the top level, and
 **Kurt Seifried \- 41:45**then everything else sort of sits under it at multiple levels, if that makes sense.
So, like, reg will be potentially directly accessible to the user.
There might also be a reg for that AI, a reg for the sub\-AI, that kind of stuff, right?
 **MatthewHoerig \- 41:58**Gotcha, Good enough, appreciate Yeah,
 **Kurt Seifried \- 42:02**because the thing is, Well, it's like the web, right?
I've in things that was like, you know, place in or do whatever.
And then, you know, and then eventually we got to Amazon.
 **MatthewHoerig \- 42:16**Right?
Yeah.
 **Kurt Seifried \- 42:20**And we're seeing, like, I'm seeing the same thing where it's I don't want to publish to WordPress.
I want to write an article and from have the whole
 **MatthewHoerig \- 42:29**kind of life cycle
 **Kurt Seifried \- 42:30**where, know, doesn't need a tweet, doesn't need an
 **MatthewHoerig \- 42:33**announcement on the blog, doesn't need all these
 **Kurt Seifried \- 42:35**other things that I want this kind of single entity just go and handle, right, like I with a human Yeah,
 **MatthewHoerig \- 42:44**cool.
Yeah.
 **Kurt Seifried \- 42:48**And that's
 **Mary Becken \- 42:51**what
 **Kurt Seifried \- 42:55**it's trying to Well, or what it's able to do.
What
 **Mary Becken \- 43:00**it's depending on, what it's, you So,
 **Kurt Seifried \- 43:04**I'm trying to teach my cat to be a shoulder cat, he's getting
 **Mary Becken \- 43:07**the hand of this But, well, and
 **Kurt Seifried \- 43:11**a good example there is, obviously, like, I wrote MCB servers early that talk to the chat GPT API and to the cloud API so that I could expressly do things like, ask both of them, like, what is a cat, and they had very
 **Mary Becken \- 43:27**culturally different approaches to answers.
Like,
 **Kurt Seifried \- 43:30**they were kind of factually correct.
but very different, as to how they talk about cats.
And so that's an example too of where at that point, like from a software bill of materials point of view, it's kind of well, for the sake of argument, if you connect to an AI agent that has some degree of autonomy, Well, well, you're like, here be dragon's because it could be whatever it was be,
right.
And then,
 **Mary Becken \- 44:00**but at least now you're informed and it's not a
 **Kurt Seifried \- 44:02**mystery.
You know.
So I that's good, maybe let's actually, maybe let's talk about that for the last 15 minutes.
So I've been thinking a lot about data flow diagrams, and I'm thinking maybe data flow diagrams.
We need something add I give it my OAuth log into Google to read my email.
 **Mary Becken \- 44:31**And in theory, that means it
 **Kurt Seifried \- 44:34**if it's using something else, that's something else could potentially use that flow.
 **Mary Becken \- 44:39**Right, yeah, exactly.
And how you're going to control that.
 **Kurt Seifried \- 44:45**Yeah.
Because, because one thing I'm seeing, a perfect example.
We use AirTable.
And AirTable, when you make a, what do they call it, personal access token or something?
Yeah, P\-A\-T, personal access token.
You can scope it to about 20 different read, write, list bases, a whole bunch of stuff.
And then you can also scope it on the other kind access to specific bases or tables.
 **Kurt Seifried \- 45:12**And so like you could have a personal access token that like read only for this one table you know, update and read for this person of stuff, whatever.
 **Mary Becken \- 45:22**But obviously not every
 **Kurt Seifried \- 45:23**API gives you that capability, right.
I also deal with a lot of vendors where it's literally like you generate an API token.
What can do?
It can do whatever it wants.
 **Mary Becken \- 45:33**Yeah.
Right?
Like within the context of my account.
 **Kurt Seifried \- 45:36**And you would
 **Mary Becken \- 45:38**oh, sorry.
So, well, and Well,
 **Kurt Seifried \- 45:41**well, but the problem is, but I could legitimately
 **Mary Becken \- 45:45**need add and remove a user.
Right, yeah.
But
 **Kurt Seifried \- 45:49**you would be careful with it, but most people
 **Mary Becken \- 45:52**would not be.
Well, but the problem is it's not me being
 **Kurt Seifried \- 45:55**careful with it.
It's the AI being careful with it.
 **Mary Becken \- 45:57**And that, you know, I was just thinking
 **Kurt Seifried \- 46:01**a developer saying, oh, let's just give it everything for a test,
 **Mary Becken \- 46:03**and then they never go back Well, well,
 **Kurt Seifried \- 46:06**I personally have a brief that says, if you click a link in Fishing and something bad happens, that's IT's fault.
you shouldn't click a link and it destroys our
 **Mary Becken \- 46:17**infrastructure and we go bankrupt.
You know, so a good example
 **Kurt Seifried \- 46:20**is I have off\-vendor backups of all our core systems, right?
We use a system called Cloud Ally obviously it's just S3 buckets, but they are a different vendor.
So even if our Google account gets deleted entirely.
We still have all our data somewhere right?
 **Mary Becken \- 46:35**Yeah.
And things like that.
So
 **Kurt Seifried \- 46:37**conveniently enough for me, it kind of meshes well with letting the AI run with scissors because I keep telling people.
I'm like, OK, worst case scenario, your AI hoses everything in air table.
We lose at most 24 hours of data, which would, don't get me wrong.
That would suck.
And a lot of people would be very upset.
 **Mary Becken \- 46:53**But it's not the end of the
 **Kurt Seifried \- 46:56**S, same thing with like, yeah, you will lose up 24 hours of email.
So, you probably don't do that, but it's not the end of the
 **Mary Becken \- 47:07**Users are going to user.
So you have plans in place.
Well,
 **Kurt Seifried \- 47:11**and realistically too, like, you know, bad things happen to good data.
But I'm thinking conceptually, we have well\-established data flow diagrams.
which traditionally sort of a bit of authentication information sort more implicitly than explicitly in my experience.
I don't think I've ever explicitly done authentication flows unless I'm doing an authentication flow diagram.
But I think what we need to do is they cannot be separate anymore, right?
The data flow and the authorization or authentication flow need to be,
 **Mary Becken \- 47:46**because it's being used as a cohesive
 **Kurt Seifried \- 47:49**whole by the AI.
Right,
 **Mary Becken \- 47:54**So.
 **Kurt Seifried \- 47:56**Yeah, I
 **Mary Becken \- 47:59**don't know what you're
 **HilsChan \- 48:02**Yeah, that's really interesting.
I was just, I'm hoping, because I'm not very knowledgeable on this, but I'm wondering how the non\-deterministic aspect of the LLM comes into this and how much you can actually map out with confidence the data flow for it, because it'd be really useful to have.
 **Kurt Seifried \- 48:20**So, With with respect to be some operations, like, is this a picture of a cat, yes or no.
And you can kind of boil it down to getting it very reliably, yes or no.
But part of the challenge give me a summary of this marketing report.
There's like no correct answer.
Right, or generate a marketing slogan Like, what's terrifying to me is like Nike, just it.
Is such a good marketing slogan.
But there theoretically, a better one out there that's even more effective, which, right, that's terrifying, because it would be like a mind worm virus.
 **Kurt Seifried \- 49:00**And so with this sort of indeterminancy, I think that speaks to having the ability to place guardrails.
So a good example would be, Oh, the MCP plug in the top to the file system.
Well, if it can talk to the part of the file system, where the MCPs are installed, like, yeah, it can now do anything because it could like write a new MCP server all bets are off.
Like, at that point, you know, what can it do?
Well, whatever it damn well wants, And so that, I think speaks to kind Like, when I'm like, oh, we run on Amazon web services, so like, we're going to ignore if the power is reliable or not.
We're just going to hope and assume that Amazon handled that properly, Because that's kind of their job as the data center provider.
And I feel kind of like the same thing with MCP servers is like, okay, oh, perfect example.
 **Kurt Seifried \- 50:03**There's a product that you still could be called manage IQ EVM.
Red Hat bought them and it got changed into cloud forms.
And it was a, essentially, it was a web\-based dashboard with API that allowed you to deploy and control cloud resources.
So like, you could give a developer access to, you know, deploy whatever in Amazon web services Cool.
And it uses Postgres SQL database as a back\-end.
And, fun fact, it uses that postgres SQL database back end with replication, also as the message bus to control all the servers.
So, for example, with this product, if you can read and write from the database,
 **HilsChan \- 50:44**well, number one, you can control all the cloud
 **Kurt Seifried \- 50:46**activity and stuff, and you can instantiate new stuff.
And obviously, you can tell the servers to do things like add and remove users or to reboot or And so I would help track that all down and understand it, maybe, right, by doing like a deep audit dive.
But then at some point, if that kind of capability exists, to put it bluntly, like,
 **HilsChan \- 51:15**well, you're up the
 **Kurt Seifried \- 51:17**creek, and maybe you don't use that product, or, you know, now you have to look at, like, guardrails.
So, so I think that's a really good question.
Yeah, because part of this is also the AI can get creative how it uses resources.
Like I
 **HilsChan \- 51:31**I've had the AI trying to escape my
 **Kurt Seifried \- 51:32**system a few times kind of accidentally.
Like, it's just trying to be really helpful.
And please stop trying to run that, know.
 **HilsChan \- 51:41**No, that makes sense, logically.
I think that's it.
And maybe it's partly my own ignorance the actual mechanism of it as well.
But it feels, even when we're talking about guardrails, it's not quite the same kind of measures that you might typically put.
in a deterministic system for you to have that.
I know that that's a hard stop for you.
You can't go any further.
 **HilsChan \- 52:03**Yeah.
 **Kurt Seifried \- 52:05**So I'm definitely still
 **HilsChan \- 52:07**struggling with being able to quantify how we would evaluate trust on that respect.
 **Kurt Seifried \- 52:13**Yeah.
I think we're all struggling.
No
 **HilsChan \- 52:16**worries.
Yeah.
I think a lot of this is going to boil
 **Kurt Seifried \- 52:19**down to Obviously there will be technical guardrails, like classic firewalls, web application firewalls.
Like a good example would be, hey, we're going to take this MCP server, run it in a container and restrict its outgoing network access to only the one approved actual database or whatever, right?
 **HilsChan \- 52:38**And we're not going to allow it to make outgoing calls to
 **Kurt Seifried \- 52:41**web servers, things like that.
But I think more fundamentally, part of the problem and part benefit is that can understand, and can work with intent.
And so think what a lot of this security, I don't know if you've read the anthropics talk about Claude's constitution.
So essentially they've taken the idea that we have to give the AI like really kind of high level guidance, like don't harm people, you know, things like and sort build a model that is smart enough to interpret that correctly hopefully not from the case of like Clod.
There's a lot of topics off the table for talking to it about.
Ironically, for example, I ran into the guardrails repeatedly.
When I was trying to talk to it about tarps the sort of thread count in tarps and how to cut them.
 **Kurt Seifried \- 53:33**And it was like, I'm not going to tell you how to cut stuff like with a knife.
Like that's, it
 **Mary Becken \- 53:37**just hit the community guidelines.
And what,
 **Kurt Seifried \- 53:40**you know, like, and I cut and paste it into chat GPT and chat GPT happily told me how to cut a tarp properly, you know, so it doesn't run or rip or whatever.
And I'm like, whatever.
And then problem went away a few weeks later with cloth.
So they obviously, you know, their guard rail went too tight and then they fixed it, right?
 **Mary Becken \- 53:58**But I think that's part of
 **Kurt Seifried \- 53:59**this people need to think about the intent of the system.
So a great example is, At the CSA, we've given a few people administrative access to our Google so that they can, you know, add and delete users.
And obviously the intent is that they do this correctly.
Like when a user joining or leaving the CSA.
They don't just randomly do it themselves, like because they feel like it or whatever, And so obviously that depends more on training because we We could in theory put some guardrail in where like, we have our HR system kind of allow an account to be deleted once the person is flagged that they've
quit or whatever.
But obviously building that would be of a pain in the butt.
 **Kurt Seifried \- 54:46**And for a small org like us, not worth it.
But for a larger org, that might be something they want to look at doing, where they kind of add this intent\-based security to their system.
another good example is like bounding.
a system might have a capability Like, a good example would be, we already have systems that can do hacking with AI, And I'm hoping, because I pay tax dollars that the Canadian government has invested money in this you know, using AI to hack the bad guys.
Same with the FBI, the NSA, CIA, whatever.
And depending on those systems, you know, like for example, they might be bounded to require like, I need a warrant from a judge to go hack this
 **Mary Becken \- 55:28**right?
Otherwise I'm not doing it because that's illegal.
 **Kurt Seifried \- 55:31**Versus like the CIA one is If the IP range, it's legal, go
 **Mary Becken \- 55:39**Well, I would hope they're doing this because
 **Kurt Seifried \- 55:41**you know, and we spend a lot of money of dollars and like they bloody well better be using the computers.
Like I'll be pissed if they're You
 **Mary Becken \- 55:46**know, we want that observability too.
Yeah.
 **Kurt Seifried \- 55:50**But I think for a lot of is, I don't want to say we're going to have to give up traditional security with AI.
But I think, but I think it's just going to be so not effective that the return on investment of doing it is very
 **Mary Becken \- 56:10**And so looking at the higher
 **Kurt Seifried \- 56:12**level, looking at the observability and transparency is the way to go.
And I also, well, and ah, good example.
Right now we have a tendency of like AI talks directly to MCP server, does stuff, comes I have a lot of what I'm looking at is, AI does stuff and then want something from the MCP, so, I think it should maybe hand it off to a second AI that expressly like has a prompt and is set up to oh, you know,
you're gonna, you're handle the data request for this AI.
And this, and so it should definitely have access to human resources and to this and to that.
But you shouldn't be looking at their personal email.
You shouldn't be doing this, you shouldn't be doing And so essentially we will have a firewall at an AI level that can understand intent and goals and will approve or disapprove that request.
 **Kurt Seifried \- 57:06**And it could even push back and say, I'm not going to do that for this reason, which could then be bubbled up to the user.
Like, hey, for example, you're asking for me to find some information on this user, but that would require me to violate their privacy.
And maybe think of argument.
The user did something illegal.
And the API came to us with a warrant and says, give us all their OK, well, we got to give them all the email, But I suspect we're going to see more intent level security because traditional security, we sort of try and apply the intent and then translate that to technical rules that, as we all
know, are always incomplete.
 **Colin Lowenberg \- 57:45**I like the concept of multiple agents, Kurt.
And I just started working for crew AI, which is a multi\-agent framework.
 **Kurt Seifried \- 57:53**And, you know, I told
 **Colin Lowenberg \- 57:56**them about the MCP working group.
in our, like,
 **Kurt Seifried \- 58:00**Our our product let's you could
 **Colin Lowenberg \- 58:03**have all the different LLMs talk to each other.
And yeah, you could set up an HR agent approves or denies requests from the other agents.
I think that's how a lot that's the future work.
It's
 **Kurt Seifried \- 58:17**like, we're not gonna have, you're gonna replace yourself with your
 **Colin Lowenberg \- 58:20**agent, but then there's human in the loop.
So one of the features that, My SEO is human in the loop.
It's like, okay,
 **Mary Becken \- 58:31**well, I don't know.
I'm like, I
 **Colin Lowenberg \- 58:35**know, but clients still want that human in the loop because they, like, we can have the traceability and the visibility into like what the agents are doing.
And that's what customers pay for, right?
They pay for that tracing and they pay for the ability to like run it in a secure, in their own environment where they have control over But they also, Like, if it more as like a coach.
Because crew loves the sports analogy.
So it's like,
 **Kurt Seifried \- 59:03**hey, time out.
Like, you should be able to call a
 **Colin Lowenberg \- 59:06**time And that's an important thing that we should implement as a rule of robotics that we didn't have before.
Like, oh, yeah, it's not just robots should not harm humans.
Is that robots should just pause whenever we say, pause, take a time because otherwise we don't have the way to like review them because they're working so much faster than we But we need to have that time out function.
And I call it human in the loop.
And I think that might the, if there's like, we need to have human in the interfere with agents at any point.
We don't agents that are no longer within our control on some AWS server that know that only one IT guy has an access to that server and can't stop the agent, right?
You
 **Kurt Seifried \- 59:55**have to be able to push the emergency
 **Colin Lowenberg \- 59:58**button or, and it's not for emergencies too.
It's also to say, hey, good job, do less of that, do more of that and give it feedback, right?
 **Kurt Seifried \- 01:00:06**So one quick comment, what you're describing sounds more like human on the loop than human in the loop.
And so difference would be is, for example, my sister and her husband work in Sketa, you know, supervisory control.
data acquisition, mostly in the oil side of things.
And my brother\-in\-in\-law actually designs the safety systems that literally,
 **Colin Lowenberg \- 01:00:25**when you hit the red button, what happens?
Because you can't just
 **Kurt Seifried \- 01:00:28**turn pumps Like, it'll get worse.
And so something to keep in mind is we can't do human in the loop, because that means by definition that your AI can only work like 40 hours
 **Colin Lowenberg \- 01:00:38**Yeah.
Explanations.
But human on the
 **Kurt Seifried \- 01:00:41**loop, you know, where people are looking at a dashboard, looking at trends, like, oh, hey, this error rate is rising.
Oh, the AI is like Brackleft
 **Colin Lowenberg \- 01:00:51**Friday sale.
That's normal.
conversely,
 **Kurt Seifried \- 01:00:54**like, the AI is confused about something and stuck in a looper.
God only knows.
So the human on the loop absolutely be what we need to shoot for, because otherwise we're crippling our systems making only as fast as humans in the loop.
The other thing is like a good example Can be a bit
 **Rajath Ravikumar \- 01:01:13**Well, yeah, well, it depends.
Like,
 **Kurt Seifried \- 01:01:14**there are certain really safety critical things where you would have a human in the loop.
Like, hey, we're going to launch the nukes.
Okay, like, Mr. President, you got to push But I mean, a good example of this is, let's I try to access a file, and the system's like, you can't access it.
And bro, I got this email from the head of marketing, you know, DKIM signed that you know, please have Kurt comment on this file.
Give me damn access to that file.
And that's the kind of thing we're also going to see, because something to keep in mind is a lot of traditional security is for like slowing down right, getting in the you know, especially with permissions and stuff.
And I think as people discover that, like we can have a smart AI that oh yeah, Kurt can read that marketing draft.
 **Kurt Seifried \- 01:02:01**Like, why not, right?
That's not a big I think we're going to see more acceptance of that because it's just going to make life so much faster, right?
Like, how much time do we all spend waiting for somebody to give us access to a document or something so that we can get our job done, But...
 **Colin Lowenberg \- 01:02:18**I love that use case of waiting for access to a document.
It's like, why can't there just be an that clicks approve?
Yes.
I've been chatting that, yes, your email is correct like, you're in the right channels.
Like you work together, you've
 **Kurt Seifried \- 01:02:32**been approved for a hundred other Google
 **Colin Lowenberg \- 01:02:35**documents in a similar fashion.
Oh, hey, you're like, five months and no one has touched in three months.
And then, like, it contains a bunch of credit card numbers.
Yeah, we're gonna review this.
Maybe you should hold off on accessing that.
Like, oh, it's been edited today, and like, you got the email, and it didn't automatically share with you.
Okay, sure, we can fix that.
 **Colin Lowenberg \- 01:03:01**Well,
 **Kurt Seifried \- 01:03:01**and that, like, I've gotten in the habit now of explicitly cutting and pasting the Google link into the email so that the Google interface is like, that link is not shared with people on this email thread.
Do you want to share it with them?
And I like, yes, like that's the whole point of me writing these stupid documents is for people to read them, right?
And I get, obviously, you know, banks and stuff can't necessarily do that.
But that, again, is where that kind of intent goes You like the AI can understand, okay, Kurt's job and position is This document is this.
The person that wrote it is this.
The context is this.
 **Kurt Seifried \- 01:03:35**based on all this information, can we make a reasonably high confident decision, yes or no?
Or do we maybe have to be like, I'm not sure.
I'm going to kick it up to a human.
And that's something to keep in mind too, right?
You can have the AI give a justification of why it whatever answer it gave and the confidence, and quite often, I will try and research something for which the AI is I just can't find enough information about that to give you a like a solid answer or a good report.
Like, it's just, you that thing doesn't really exist yet, so good luck.
You know, I'm like, okay, now I got to do my job, right?
 **Kurt Seifried \- 01:04:18**But, okay, so well, I'm going to, I think the marketing, the marketplace kind of list of things to look at is reasonably complete.
Like I said, I'm gonna have the AI go through and do a bunch more.
I've already had the AI do a bunch of these, but I'm gonna have a go do a bit more Next meeting, we'll talk about the MCP client checklist that we want.
And I think, now that you mentioned it, Why can't the client generate sort of a data flow diagram and off flow diagram.
Here's a good example.
Should an MCP client have a button where I can basically say like tell me everything you have access to and what level of access you have so that I can like double check and audit As far as I know, that does not exist.
Like I'd have to click through a bunch of interfaces and claw desktop and like pick snapshots.
 **Kurt Seifried \- 01:05:09**You so yeah.
And then also this data flow and off flow thing.
I'm gonna think about that a bit.
I'll email the But
 **HilsChan \- 01:05:19**yeah.
One interesting thing, my
 **Colin Lowenberg \- 01:05:22**product lets you generate an MCP server from your crew of AI agents.
So
 **Kurt Seifried \- 01:05:27**I'm trying to dive into it and understand it better,
 **Colin Lowenberg \- 01:05:29**but like, this is how people can, like a bunch of enterprises use our product and they can just export to MCP.
and then share that.
It's just a portable MCP server they could just run anywhere.
So
 **Kurt Seifried \- 01:05:40**it's like, you can just, it's just a Python
 **Colin Lowenberg \- 01:05:42**agent team.
And maybe I should see how we do it.
And if we follow the best practices for security.
 **Kurt Seifried \- 01:05:50**Yeah.
Well, and that's a great example.
That's what I want.
I don't want to talk to my WordPress server.
I want the AI to help me write a blog article and then do all the marketing side of it and posting it and blah, blah.
Like, don't bug me it.
And yeah, like, that's what people are building.
 **Kurt Seifried \- 01:06:07**So thanks, everybody.
Does anybody have any last minute questions or concerns?
Before I am call.
sold.
cool.
Well, thank you, everybody.
I'll see you, I guess, next meeting.
 **Kurt Seifried \- 01:06:27**And also, we have the Slack channel, obviously, which I need to be more active And yeah, I guess that's Thanks.
Bye,
 **MatthewHoerig \- 01:06:40**Yeah.
Talk to you, Take Amen.
 **Kurt Seifried \- 01:06:45**The recording has stopped.
