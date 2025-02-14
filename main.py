import random;

who = ['My cat', 'The delivery guy', 'A ghost', 'My brother'];
what = ['burned', 'dropped', 'spilled', 'lost'];
when = ['before turning it in', 'right when I needed it', 'while I was sleeping', 'when I was in the bathroom', 'while I was doing something else'];

excuse_created = random.choice(who) + " " + random.choice(what) + " " + random.choice(when) + ".";

print(excuse_created)