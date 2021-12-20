using Xamarin.Forms;

namespace Musofirlar.uz.Views
{
    public partial class EmbassyPage : ContentPage
    {
        public EmbassyPage()
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