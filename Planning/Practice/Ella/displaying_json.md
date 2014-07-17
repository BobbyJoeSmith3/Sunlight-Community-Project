displaying_json.md

{
	{
		bill-Name:asgddsg,
		state:va,
		party:dem
	},
	{
		bill-Name:asgddsg,
		state:va,
		party:dem
	},
	{
		bill-Name:asgddsg,
		state:va,
		party:dem
	},
	{
		bill-Name:asgddsg,
		state:va,
		party:dem
	},
	{
		bill-Name:asgddsg,
		state:va,
		party:dem
	},
	{
		bill-Name:asgddsg,
		state:va,
		party:dem
	},

}

results = r.text.json()

for x in results:





<li>
	<h3>{{x.symbol}}</h3>
	<h2>{{x.exchange}} -- {{{x.currentPrice.Amount}}</h2>
</li>