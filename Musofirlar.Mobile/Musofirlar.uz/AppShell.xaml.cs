using Musofirlar.uz.Views;
using Xamarin.Forms;

namespace Musofirlar.uz
{
    public partial class AppShell : Xamarin.Forms.Shell
    {
        public AppShell()
        {
            InitializeComponent();
            Routing.RegisterRoute("flat", typeof(RentPage));
        }
        protected override void OnNavigating(ShellNavigatingEventArgs args)
        {
            base.OnNavigating(args);

            if (args.Source == ShellNavigationSource.Pop)
            {
                args.Cancel();
            }
        }
    }
}
