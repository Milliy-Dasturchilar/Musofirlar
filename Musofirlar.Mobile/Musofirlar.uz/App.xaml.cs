using Musofirlar.uz.Views;
using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using Xamarin.Essentials;

namespace Musofirlar.uz
{
    public partial class App : Application
    {

        public App()
        {
            InitializeComponent();

            if (Device.RuntimePlatform == Device.UWP)
            {
                MainPage = new AppShell();
            }
            else
            {
                MainPage = new SplashPage();
            }
        }

        protected override void OnStart()
        {
        }

        protected override void OnSleep()
        {
        }

        protected override void OnResume()
        {
            
        }
    }
}
