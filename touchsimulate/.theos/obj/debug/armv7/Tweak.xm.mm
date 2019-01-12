#line 1 "Tweak.xm"
OBJC_EXTERN UIImage *_UICreateScreenUIImage(void);

@interface SpringBoard : UIApplication
@end


#include <substrate.h>
#if defined(__clang__)
#if __has_feature(objc_arc)
#define _LOGOS_SELF_TYPE_NORMAL __unsafe_unretained
#define _LOGOS_SELF_TYPE_INIT __attribute__((ns_consumed))
#define _LOGOS_SELF_CONST const
#define _LOGOS_RETURN_RETAINED __attribute__((ns_returns_retained))
#else
#define _LOGOS_SELF_TYPE_NORMAL
#define _LOGOS_SELF_TYPE_INIT
#define _LOGOS_SELF_CONST
#define _LOGOS_RETURN_RETAINED
#endif
#else
#define _LOGOS_SELF_TYPE_NORMAL
#define _LOGOS_SELF_TYPE_INIT
#define _LOGOS_SELF_CONST
#define _LOGOS_RETURN_RETAINED
#endif

@class Springboard; 
static void (*_logos_orig$_ungrouped$Springboard$applicationDidFinishLaunching$)(_LOGOS_SELF_TYPE_NORMAL Springboard* _LOGOS_SELF_CONST, SEL, id); static void _logos_method$_ungrouped$Springboard$applicationDidFinishLaunching$(_LOGOS_SELF_TYPE_NORMAL Springboard* _LOGOS_SELF_CONST, SEL, id); 

#line 6 "Tweak.xm"

static void _logos_method$_ungrouped$Springboard$applicationDidFinishLaunching$(_LOGOS_SELF_TYPE_NORMAL Springboard* _LOGOS_SELF_CONST __unused self, SEL __unused _cmd, id application) {
  
  
  
  
  
  
  
  
  
  
  
  
  

	HBLogDebug(@"-[<Springboard: %p> applicationDidFinishLaunching:%@]", self, application);
	NSLog(@"**********************************************************************************");
	NSLog(@"****************************************** SUCCESS *******************************");
	NSLog(@"**********************************************************************************");

	_logos_orig$_ungrouped$Springboard$applicationDidFinishLaunching$(self, _cmd, application);

	
	
}

























static __attribute__((constructor)) void _logosLocalInit() {
{Class _logos_class$_ungrouped$Springboard = objc_getClass("Springboard"); MSHookMessageEx(_logos_class$_ungrouped$Springboard, @selector(applicationDidFinishLaunching:), (IMP)&_logos_method$_ungrouped$Springboard$applicationDidFinishLaunching$, (IMP*)&_logos_orig$_ungrouped$Springboard$applicationDidFinishLaunching$);} }
#line 57 "Tweak.xm"
