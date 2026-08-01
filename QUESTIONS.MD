 **BillShock** is a consumer-focused app that estimates and forecasts electricity costs by combining **appliance recognition/input**, **usage-time tracking**, and **dynamic Meralco kWh rate integration**. The Meralco API you linked provides current Meralco residential rates, including endpoints like `/rates`, `/rates/typical`, and `/rates/<kwh>`, with data such as PHP/kWh rate, monthly change, percent change, and trend. [\[github.com\]](https://github.com/rairulyle/meralco-ph/)

To complete this into a strong thesis proposal, I’ll ask you the important questions by section. Sagutin mo lang kahit bullet form. After that, I can help you turn it into a full proposal with **background, objectives, scope, methodology, system architecture, and expected output**.

***

# Questions to Complete the Thesis Proposal

## 1. Main Problem / Research Gap

1. Ano ang main problem na gusto mong i-solve?
   * Mataas na electric bill?
   * Hindi alam ng consumers kung aling appliance ang malakas kumonsumo?
   * Walang real-time estimate bago dumating ang Meralco bill?
   * Hirap mag-budget ng monthly electricity expenses?

2. Gusto mo bang i-position ang app as:
   * **electricity bill estimator**
   * **appliance consumption tracker**
   * **cost forecasting tool**
   * or all of the above?

3. May existing apps ka bang gustong i-compare against?
   * Meralco app?
   * Manual bill calculators?
   * Smart plugs?
   * Home Assistant energy dashboards?

***

## 2. Target Users

4. Sino ang exact users?
   * Meralco residential customers only?
   * Students/boarders?
   * Household owners?
   * Renters?
   * Small apartment/unit owners?

5. Need ba ng user account/login?
   * Yes, para ma-save appliance list and calendar history?
   * No, local/device-based lang?

6. Ilang user type ang meron?
   * Regular consumer only?
   * Admin?
   * Researcher/tester?

***

## 3. Appliance Recognition Feature

7. Kapag nag-scan ng appliance picture, ano ang expected output?
   Example:
   * Appliance type: electric fan
   * Estimated wattage: 60W
   * Suggested usage category: low consumption
   * Confidence score: 85%

8. Image recognition ba ay:
   * appliance type recognition only?
   * brand/model recognition?
   * OCR reading ng label/nameplate?
   * both image classification and OCR?

9. If hindi makita sa picture ang wattage, saan manggagaling ang wattage?
   * Built-in appliance database?
   * User manual input?
   * Internet/API search?
   * Average wattage table?

10. Anong appliances ang covered sa prototype?
    Suggested scope:

* electric fan
* refrigerator
* air conditioner
* rice cooker
* washing machine
* TV
* laptop/PC
* phone charger
* microwave
* iron

11. Ilang appliance categories ang kaya mong i-support sa thesis prototype?

***

## 4. Manual Input Feature

12. Kapag manual input, anong details hihingin?
    Suggested:

* Appliance name
* Brand/model
* Wattage
* Quantity
* Usage start time
* Usage end time
* Frequency: daily/weekly/custom
* Room/location, optional

13. Kapag model lang ang nilagay, gusto mo ba na app will try to auto-suggest wattage?

14. Papayagan ba ang user na i-edit ang suggested wattage?

***

## 5. Usage Tracking

15. Paano iti-track ang usage time?

* Manual start/stop button?
* User inputs start and end time?
* Calendar-based schedule?
* Timer mode?

16. If nakalimutan ng user mag-stop, ano mangyayari?

* Auto-reminder?
* Maximum default time?
* User can edit later?

17. Daily ba ang tracking or per appliance session?
    Example:

* Electric fan: 8:00 PM–6:00 AM
* Rice cooker: 6:00 AM–6:45 AM

18. Need ba ng notification/reminder?
    Example: “Your AC has been running for 5 hours. Estimated cost: ₱\_\_\_.”

***

## 6. Calendar-Based Consumption

19. Ano ang calendar view?

* Daily total cost?
* Appliance usage per day?
* Monthly projected bill?
* Color-coded days based on high/low usage?

20. Ano ang gusto mong makita sa calendar?
    Example:

* June 1: ₱120 estimated usage
* June 2: ₱135 estimated usage
* Appliance breakdown per day

21. Need ba ng monthly summary?

* Total kWh consumed
* Total estimated cost
* Highest consuming appliance
* Average daily cost
* Forecasted end-of-month bill

***

## 7. Cost Formula and Forecasting

Your current formula is good:

```text
Cost = (Wattage × Hours Used / 1000) × Current Meralco Rate per kWh
```

22. Forecasting will be based on what?

* Average daily consumption × remaining days of month?
* Calendar schedule?
* Past usage history?
* Fixed appliance pattern?

23. Gusto mo ba ng forecast like:

* “If you continue this usage pattern, your estimated bill by month-end is ₱\_\_\_\_.”
* “Your current trend is 12% higher than last week.”
* “Most expensive appliance this month: Air Conditioner.”

24. Isasama ba sa computation ang other Meralco bill components?

* Generation charge
* Transmission charge
* Distribution charge
* Taxes
* System loss
* Universal charges

Or simple final PHP/kWh rate from API lang?

The API you linked says it returns final per-kWh rates at different consumption levels, including typical 200 kWh household rate and specific kWh levels like 50, 100, 200, 300, 500, etc. [\[github.com\]](https://github.com/rairulyle/meralco-ph/)

***

## 8. Meralco API Integration

25. Which rate will your app use as default?

* `/rates/typical` or 200 kWh typical household?
* `/rates/<kwh>` depending on user’s expected monthly consumption?

26. If API is unavailable, what fallback?

* Last saved Meralco rate?
* Manual rate input?
* Default sample rate?

27. Since API is not official Meralco, okay ba sa thesis mo na third-party API ito?
    The repository states that it parses publicly available Meralco electricity rate schedule PDFs and is not affiliated with or endorsed by Meralco. [\[github.com\]](https://github.com/rairulyle/meralco-ph/)

28. Should the system show a disclaimer?
    Example:

> “Estimated cost only. Actual Meralco bill may vary depending on taxes, charges, and billing adjustments.”

***

## 9. AI / Algorithm Part

29. What AI approach do you want to use?

* Image classification model?
* OCR-based extraction?
* Pre-trained model like MobileNet/EfficientNet?
* Cloud vision API?
* Custom trained model?

30. For thesis feasibility, do you want:

* **Prototype-level AI**, using pre-trained image recognition + database matching?
* or **custom-trained AI model** with your own dataset?

31. Do you already have appliance image dataset?

* Yes
* No
* Need to collect

32. If no dataset, are you willing to limit the system to common appliance categories?

***

## 10. Platform

33. Ano ang platform?

* Android app?
* Web app?
* Progressive Web App?
* Desktop app?

34. If mobile app, anong stack?

* Flutter?
* React Native?
* Android Studio/Kotlin?
* Web-based with camera upload?

35. Need ba ng camera access?

* live scan
* upload image only
* both

***

## 11. Database

36. Ano ang ise-save sa database?
    Suggested:

* User profile
* Appliance list
* Appliance wattage
* Usage logs
* Daily cost
* Monthly forecast
* Meralco rate history

37. Local database lang ba or cloud database?

* Firebase?
* Supabase?
* MySQL?
* SQLite?

***

## 12. System Outputs

38. Ano ang final output ng system?
    Example:

* Real-time estimated cost
* Daily consumption report
* Monthly bill forecast
* Appliance consumption ranking
* Calendar-based usage log
* Energy-saving recommendations

39. Need ba ng downloadable report?

* PDF monthly report?
* CSV export?
* Screenshot summary?

40. Need ba ng recommendations?
    Example:

* “Reducing AC usage by 1 hour per day may save around ₱\_\_\_ per month.”

***

## 13. Thesis Scope and Limitations

41. Ano ang hindi covered?
    Suggested limitations:

* Hindi actual smart meter reading
* Hindi official Meralco billing system
* Estimates only
* Appliance wattage may vary by model, condition, and usage mode
* AI recognition limited to selected appliance categories
* Internet required for updated Meralco rate API

42. Will the app work offline?

* Yes, but uses last saved rate
* No, needs internet

43. Will it detect actual power draw?

* No, estimated based on wattage and time
* Yes, if connected to smart plug, but this may be too much for thesis scope

***

## 14. Evaluation / Testing

44. Paano mo i-evaluate ang app?
    Suggested:

* Accuracy of appliance recognition
* Accuracy of cost computation
* User satisfaction survey
* Usability testing
* Comparison with manual computation

45. Ilang respondents ang target mo?

* 10?
* 20?
* 30?
* Meralco customers only?

46. What metrics will you use?
    Example:

* Recognition accuracy
* Computation correctness
* Forecast error percentage
* SUS usability score
* User acceptance rating

47. Will you compare estimated bill vs actual Meralco bill?
    This would strengthen the study, but you need user consent and sample billing data.

***

# Suggested Refined Title Options

Your current title is good, but we can polish it:

## Option 1

**BillShock: A Kilowatt-Hour Monitoring and Electricity Cost Forecasting Application Using Appliance Image Recognition and Dynamic Meralco Rate API Integration**

## Option 2

**BillShock: An AI-Assisted Appliance Consumption Monitoring and Electricity Cost Forecasting Application for Meralco Consumers**

## Option 3

**BillShock: A Calendar-Based Electricity Consumption Tracker with Appliance Recognition and Dynamic kWh Rate Integration**

My recommended title:

> **BillShock: An AI-Assisted Appliance Consumption Monitoring and Electricity Cost Forecasting Application Using Dynamic Meralco Rate Integration**

Mas thesis-friendly siya kasi clear ang AI, monitoring, forecasting, and Meralco integration.

***

# Quick Answer Template

Para mabilis, sagutin mo ito:

```text
1. Platform:
2. Target users:
3. Appliance categories:
4. AI method:
5. Image scan output:
6. Manual input details:
7. Usage tracking method:
8. Calendar features:
9. Forecasting method:
10. Meralco API rate to use:
11. Database:
12. Reports/outputs:
13. Scope limitations:
14. Evaluation method:
15. Preferred final title:
```

