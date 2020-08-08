# Experimentation

## Blocks

In blocks it ended up coming out as a blob so I added a 1px separation between each block in the stack so you can see it easily

## Snowman

I experimented with anchoring all the snowmen at the same y coordinate using an equation - which worked well and perfectly. However I noticed
that this wasn't stated in the question and other students hadn't done it so I just used a fixed y offset (which is basically perfect anyway, and less complicated)

I also experimented with calculating if the snowmen went off screen at all whether to hide them (instead of being able to be half on/off) but due to the 
'social distancing' offset I added there was no point

I also (messily) added specific `int()` statements to the snowman position due to a warning about how implicit int conversion may be removed in future.
 
## Sierpinski

This was pretty straightforward. I was confused at first as to why it wasn't working and then realised I forgot to add an inverse triangle on top of the white so we could see
where new triangles were created. 

In theory this could be more efficient by just drawing the initial (base) white triangle and from there ONLY drawing the inverse green triangles...
I just didn't do this because it seemed beyond the scope of this specific task and wasn't asked for.

I also chose green for the inverse triangle colour. I messed around with the minimum size until I found one that was performant, still looked decent but also showed
the full pattern over as many recursions as possible.

I did initially have an issue with the inverse trianlge shape being of a m/2 gradient to what they were supposed to - this is because I was using (size/2)-x instead of (size/2)+x

## Others

I also did the other two optional tasks and they were pretty straightforward

## Conclusion

This was the 'funnest' (great english) workshop I've done out of 171 and 172 so far. Visualising things is quite satisfying. Thanks for all your effort!