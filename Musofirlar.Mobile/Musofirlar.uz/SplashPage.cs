using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Forms;

namespace Musofirlar.uz
{
    public class SplashPage : ContentPage
    {
        Image splashImage;

        public SplashPage()
        {
            NavigationPage.SetHasNavigationBar(this, false);
            var sub = new AbsoluteLayout();
            splashImage = new Image
            {
                Source = "icon.png",
                WidthRequest = 150,
                HeightRequest = 150
            };
            AbsoluteLayout.SetLayoutFlags(splashImage,
               AbsoluteLayoutFlags.PositionProportional);
            AbsoluteLayout.SetLayoutBounds(splashImage,
             new Rectangle(0.5, 0.5, AbsoluteLayout.AutoSize, AbsoluteLayout.AutoSize));

            sub.Children.Add(splashImage);

            this.BackgroundColor = Color.FromHex("#27AAE1");
            this.Content = sub;
        }
        protected override async void OnAppearing()
        {
            base.OnAppearing();

            await splashImage.ScaleTo(1, 1000);

            await splashImage.RotateTo(720, 500, Easing.Linear);
            await splashImage.ScaleTo(0, 500, Easing.Linear);


            Application.Current.MainPage = new AppShell();
        }
    }
}
