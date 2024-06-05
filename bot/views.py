from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage

def generate_bot_response(user_message):
    # Your custom logic to generate bot response based on user input
    # This is just a placeholder example
    if 'hello' in user_message.lower():
        return "Hello! How can I assist you today?"
    
    elif 'revenue generated from haircare products' in user_message.lower():
        return "The total revenue generated from haircare products is $40,919.39."
    
    elif 'highest average price per unit' in user_message.lower():
        return "the cosmetics category has the highest average price per unit ($59.68)."

    elif 'how many units of sku94 (cosmetics) were sold' in user_message.lower():
        return "987 units of SKU94 were sold."
    
    elif 'what is the top revenue generating supplier' in user_message.lower():
        return "supplier 3 is the top revenue generating supplier with $20,726.96 in revenue."
    
    elif 'which carrier was used the most' in user_message.lower():
        return "carrier b was used the most in 13 transactions."
    
    elif 'what is the average shipping cost per transaction' in user_message.lower():
        return "the average shipping cost per transaction is $59.34."
    
    elif 'how many transactions used the rail shipping mode' in user_message.lower():
        return "11 transactions used the rail shipping mode."
    
    elif 'what is the total sales revenue from skincare products' in user_message.lower():
        return "the total sales revenue from skincare products is $33,594.04."
    
    elif 'which product category has the highest quantity available' in user_message.lower():
        return "haircare products have the highest quantity available."
    
    elif 'what is the average lead time for shipping' in user_message.lower():
        return "the average lead time for shipping is 16.66 days."
    
    elif 'how many transactions had a stock status of pending' in user_message.lower():
        return "there were 8 transactions with a stock status of pending."
    
    elif 'which shipping route was used the most' in user_message.lower():
        return "route b was used the most in 11 transactions."
    
    elif 'what is the total revenue generated from cosmetics products' in user_message.lower():
        return "the total revenue generated from cosmetics products is $43,693.79."
    
    elif 'how many units of sku99 (haircare) were sold' in user_message.lower():
        return "627 units of sku99 were sold."
    
    elif 'which customer gender made the most purchases' in user_message.lower():
        return "non-binary customers made the most purchases."
    
    elif 'what is the average discount percentage per transaction' in user_message.lower():
        return "the average discount percentage per transaction is calculated by adding up all the discount percentages and dividing by the total number of transactions."
    elif 'what is the total revenue generated from male customers' in user_message.lower():
        return "the total revenue generated from male customers can be calculated by summing up the revenue from transactions where the customer gender is male."
    elif 'which supplier had the highest average customer rating' in user_message.lower():
        return "calculate the average customer rating for each supplier and identify the one with the highest average."
        
    elif 'what is the total revenue generated from transactions with a stock status of pass' in user_message.lower():
        return "sum up the revenue from transactions where the stock status is pass."
    
    elif 'how many transactions had a stock status of fail and used carrier b for shipping' in user_message.lower():
        return "count the number of transactions where the stock status is fail and the carrier used is carrier b."
    else:
        print("Debug: User message:", user_message.lower())  # Debugging statement
        return "I'm sorry, I didn't understand that. Could you please rephrase?"
    
    
def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        ChatMessage.objects.create(user='User', message=user_message)
        bot_response = generate_bot_response(user_message)
        ChatMessage.objects.create(user='Bot', message=bot_response)
        return JsonResponse({'response': bot_response})
    else:
        # Clear existing chat messages when the view is loaded
        ChatMessage.objects.all().delete()
        default_response = "Hello! This is ChatBot, How can I assist you today?"
        ChatMessage.objects.create(user='Bot', message=default_response)
        chat_messages = ChatMessage.objects.all()
        return render(request, 'chatbot/chat.html', {'chat_messages': chat_messages})
