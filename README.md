<H1>Weather Predict</H1>
<H2>CSCI 141 "Research Project" </H2>
<H2>Brenna Nieva</H2>



<H2>Description</H2>

<H2>Table of Contents</H2>
<h2>Installation</h2>
<h2>Usage</h2>
<h2>Contributing</h2>
<h2>Credits</h2>
<h2>License</h2>


<H2>Updates</h2>
<h3>10/15/2019</h3>


**Goals:**
* guessing tomorrow's temperature based on yesterday's and today's
* estimating probability of precipitation and/or cloud cover based on barometric pressure
* using a nearest-neighbor classification to predict what the weather will be tomorrow

**Data:**
*daily high and low temperatures
*pressure
*wind direction
*cloud cover
*precipitation

I'd start with a year's worth of daily data for Bellingham and start trying out some ideas on that.


10/20
data downloaded and into some format that can be manipulated easily

try out some very simple predictions for temperature, such as:
Assume temp will be the same: tomorrow_prediction = today
Assume temp will continue the trend from the past two days: tomorrow_prediction = today + (today - yesterday).
</p>