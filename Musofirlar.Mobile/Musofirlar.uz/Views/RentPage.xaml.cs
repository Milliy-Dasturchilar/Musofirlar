using Xamarin.Forms;

namespace Musofirlar.uz.Views
{
    public partial class RentPage : ContentPage
    {
        public RentPage()
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