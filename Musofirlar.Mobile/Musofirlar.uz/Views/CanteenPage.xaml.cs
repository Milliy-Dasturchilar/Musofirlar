using Xamarin.Forms;

namespace Musofirlar.uz.Views
{
    public partial class CanteenPage : ContentPage
    {
        public CanteenPage()
        {
            InitializeComponent();
        }

        void webviewNavigating(object sender, WebNavigatingEventArgs e)
        {
            labelLoading.IsVisible = true;
        }

        void webviewNavigated(object sender, WebNavigatedEventArgs e)
        {
            labelLoading.IsVisible = false;
        }
    }
}