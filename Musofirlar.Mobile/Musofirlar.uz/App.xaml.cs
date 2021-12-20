using Musofirlar.uz.Services;
using Musofirlar.uz.Views;
using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Musofirlar.uz
{
    public partial class App : Application
    {

        public App()
        {
            InitializeComponent();

            DependencyService.Register<MockDataStore>();
            MainPage = new AppShell();
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
