from django.shortcuts import render, redirect 
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
	# grab the data from api
	import requests
	# parse the data from the api
	import json

	if request.method == 'POST':
		# this ticker is the name of that form in base.html
		# if user types in goog, itll become goog
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_741778199c504a6da0904a0a844874af")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api' : api})
	else:
		return render(request, 'home.html', {'ticker' : "Enter a ticker symbol above..."})

	# pk_741778199c504a6da0904a0a844874af
	# create a request
	#api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_741778199c504a6da0904a0a844874af")
	
	# connect the api (with redudancy), wrap it in python error block
	#try:
	#	api = json.loads(api_request.content)
	#except Exception as e:
	#	api = "Error..."

	# pass the api variable into our homepage
	#return render(request, 'home.html', {'api' : api})

def about(request):
	return render(request, 'about.html', {})
	

def add_stock(request):
	import requests
	import json

	# use built in django form system
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added!!"))
			return redirect('add_stock')
	else:
		# pull stuff out of the database
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_741778199c504a6da0904a0a844874af")

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
	# pk means primary key, which in this case is the stock id number
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock has been deleted!"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})