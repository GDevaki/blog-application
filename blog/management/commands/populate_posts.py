from typing import Any
from blog.models import category,Post
from django.core.management.base import BaseCommand
import random
class Command(BaseCommand):
    help="This command inserts post data"

    def handle(self, *args:Any, **options:Any):
        Post.objects.all().delete()
        titles=[
    "10 Simple Habits That Can Change Your Life Forever",
"How to Declutter Your Mind and Home in 30 Days",
"Morning Routines of Successful People You Can Try Today",
"The Ultimate Guide to Traveling on a Budget",
"Hidden Gems: 7 Underrated Travel Destinations to Visit in 2024",
"How to Pack Light for Any Trip Without Sacrificing Essentials",
"Top 5 AI Tools That Can Save You Time and Boost Productivity",
"The Future of Renewable Energy: What to Expect in the Next Decade",
"Beginner’s Guide to Building Your Own Smart Home",
"Plant-Based Diets: Benefits, Challenges, and Easy Recipes",
"The Science Behind Sleep and How to Improve Yours Tonight",
"At-Home Workouts: Quick Routines for Busy Professionals"
]

        contents=[
    "Discover small, actionable habits to boost productivity, happiness, and well-being.",
"A step-by-step guide to achieving mental clarity and an organized living space.",
"Learn proven morning habits that set high achievers up for success.",
"Tips and tricks for exploring the world without breaking the bank.",
"Unique and lesser-known locations to add to your travel bucket list.",
"Master the art of packing smartly for stress-free travel experiences.",
"Explore cutting-edge tools to simplify tasks and supercharge efficiency.",
"Insights into upcoming trends and innovations shaping sustainable energy.",
"An easy introduction to transforming your house with smart technology.",
"Everything you need to know to start and maintain a plant-based lifestyle.",
"Practical strategies to enhance sleep quality and wake up refreshed.",
"Efficient exercise plans to stay fit without leaving the comfort of home."
]

        img_urls=[
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400"
]

        categories=category.objects.all()
        for title,content,img_url in zip(titles,contents,img_urls):
            Category=random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=Category)

        self.stdout.write(self.style.SUCCESS("Completed inerting data!"))