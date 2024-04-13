import random
from pyrogram import Client, filters
from pyrogram import Client 
from SEMO.info import (joinch)
from pyrogram.types import Message
from pyrogram import enums


kurok = [" |  بين الإبحار لمدة أسبوع كامل أو السفر على متن طائرة لـ 3 أيام متواصلة؟ ",
" |  بين شراء منزل صغير أو استئجار فيلا كبيرة بمبلغ معقول؟ ",
" |  أن تعيش قصة فيلم هل تختار الأكشن أو الكوميديا؟ ",
" |  بين تناول البيتزا وبين الايس كريم وذلك بشكل دائم؟ ",
" |  بين إمكانية تواجدك في الفضاء وبين إمكانية تواجدك في البحر؟ ",
" |  بين تغيير وظيفتك كل سنة أو البقاء بوظيفة واحدة طوال حياتك؟ ",
" |  أسئلة محرجة أسئلة صراحة ماذا ستختار؟ ",
" |  بين الذهاب إلى الماضي والعيش مع جدك أو بين الذهاب إلى المستقبل والعيش مع أحفادك؟ ",
"لو كنت شخص اخر هل تفضل البقاء معك أم أنك ستبتعد عن نفسك؟ ",
" |  بين الحصول على الأموال في عيد ميلادك أو على الهدايا؟ ",
" |  بين القفز بمظلة من طائرة أو الغوص في أعماق البحر؟ ",
" |  بين الاستماع إلى الأخبار الجيدة أولًا أو الاستماع إلى الأخبار السيئة أولًا؟ ",
" |  بين أن تكون رئيس لشركة فاشلة أو أن تكون موظف في شركة ناجحة؟ ",
" |  بين أن يكون لديك جيران صاخبون أو أن يكون لديك جيران فضوليون؟ ",
" |  بين أن تكون شخص مشغول دائمًا أو أن تكون شخص يشعر بالملل دائمًا؟ ",
" |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ ",
" |  بين استمرار فصل الشتاء دائمًا أو بقاء فصل الصيف؟ ",
" |  بين العيش في القارة القطبية أو العيش في الصحراء؟ ",
" |  بين أن تكون لديك القدرة على حفظ كل ما تسمع أو تقوله وبين القدرة على حفظ كل ما تراه أمامك؟ ",
" |  بين أن يكون طولك 150 سنتي متر أو أن يكون 190 سنتي متر؟ ",
" |  بين إلغاء رحلتك تمامًا أو بقائها ولكن فقدان الأمتعة والأشياء الخاص بك خلالها؟ ",
" |  بين أن تكون اللاعب الأفضل في فريق كرة فاشل أو أن تكون لاعب عادي في فريق كرة ناجح؟ ",
" |  بين ارتداء ملابس البيت لمدة أسبوع كامل أو ارتداء البدلة الرسمية لنفس المدة؟ ",
" |  بين امتلاك أفضل وأجمل منزل ولكن في حي سيء أو امتلاك أسوأ منزل ولكن في حي جيد وجميل؟ ",
" |  بين أن تكون غني وتعيش قبل 500 سنة، أو أن تكون فقير وتعيش في عصرنا الحالي؟ ",
" |  بين ارتداء ملابس الغوص ليوم كامل والذهاب إلى العمل أو ارتداء ملابس جدك/جدتك؟ ",
" |  بين قص شعرك بشكل قصير جدًا أو صبغه باللون الوردي؟ ",
" |  بين أن تضع الكثير من الملح على كل الطعام بدون علم أحد، أو أن تقوم بتناول شطيرة معجون أسنان؟ ",
" |  بين قول الحقيقة والصراحة الكاملة مدة 24 ساعة أو الكذب بشكل كامل مدة 3 أيام؟ ",
" |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟ ",
" |  بين وضع أحمر الشفاه على وجهك ما عدا شفتين أو وضع ماسكارا على شفتين فقط؟ ",
" |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟ ",
" |  بين تلوين شعرك كل خصلة بلون وبين ارتداء ملابس غير متناسقة لمدة أسبوع؟ ",
" |  بين تناول مياه غازية مجمدة وبين تناولها ساخنة؟ ",
" |  بين تنظيف شعرك بسائل غسيل الأطباق وبين استخدام كريم الأساس لغسيل الأطباق؟ ",
" |  بين تزيين طبق السلطة بالبرتقال وبين إضافة البطاطا لطبق الفاكهة؟ ",
" |  بين اللعب مع الأطفال لمدة 7 ساعات أو الجلوس دون فعل أي شيء لمدة 24 ساعة؟ ",
" |  بين شرب كوب من الحليب أو شرب كوب من شراب عرق السوس؟ ",
" |  بين الشخص الذي تحبه وصديق الطفولة؟ ",
" |  بين أمك وأبيك؟ ",
" |  بين أختك وأخيك؟ ",
" |  بين نفسك وأمك؟ ",
" |  بين صديق قام بغدرك وعدوك؟ ",
" |  بين خسارة حبيبك/حبيبتك أو خسارة أخيك/أختك؟ ",
" |  بإنقاذ شخص واحد مع نفسك بين أمك أو ابنك؟ ",
" |  بين ابنك وابنتك؟ ",
" |  بين زوجتك وابنك/ابنتك؟ ",
" |  بين جدك أو جدتك؟ ",
" |  بين زميل ناجح وحده أو زميل يعمل كفريق؟ ",
" |  بين لاعب كرة قدم مشهور أو موسيقي مفضل بالنسبة لك؟ ",
" |  بين مصور فوتوغرافي جيد وبين مصور سيء ولكنه عبقري فوتوشوب؟ ",
" |  بين سائق سيارة يقودها ببطء وبين سائق يقودها بسرعة كبيرة؟ ",
" |  بين أستاذ اللغة العربية أو أستاذ الرياضيات؟ ",
" |  بين أخيك البعيد أو جارك القريب؟ ",
" |  يبن صديقك البعيد وبين زميلك القريب؟ ",
" |  بين رجل أعمال أو أمير؟ ",
" |  بين نجار أو حداد؟ ",
" |  بين طباخ أو خياط؟ ",
" |  بين أن تكون كل ملابس بمقاس واحد كبير الحجم أو أن تكون جميعها باللون الأصفر؟ ",
" |  بين أن تتكلم بالهمس فقط طوال الوقت أو أن تصرخ فقط طوال الوقت؟ ",
" |  بين أن تمتلك زر إيقاف موقت للوقت أو أن تمتلك أزرار للعودة والذهاب عبر الوقت؟ ",
" |  بين أن تعيش بدون موسيقى أبدًا أو أن تعيش بدون تلفاز أبدًا؟ ",
" |  بين أن تعرف متى سوف تموت أو أن تعرف كيف سوف تموت؟ ",
" |  بين العمل الذي تحلم به أو بين إيجاد شريك حياتك وحبك الحقيقي؟ ",
" |  بين معاركة دب أو بين مصارعة تمساح؟ ",
" |  بين إما الحصول على المال أو على المزيد من الوقت؟ ",
" |  بين امتلاك قدرة التحدث بكل لغات العالم أو التحدث إلى الحيوانات؟ ",
" |  بين أن تفوز في اليانصيب وبين أن تعيش مرة ثانية؟ ",
" |  بأن لا يحضر أحد إما لحفل زفافك أو إلى جنازتك؟ ",
" |  بين البقاء بدون هاتف لمدة شهر أو بدون إنترنت لمدة أسبوع؟ ",
" |  بين العمل لأيام أقل في الأسبوع مع زيادة ساعات العمل أو العمل لساعات أقل في اليوم مع أيام أكثر؟ ",
" |  بين مشاهدة الدراما في أيام السبعينيات أو مشاهدة الأعمال الدرامية للوقت الحالي؟ ",
" |  بين التحدث عن كل شيء يدور في عقلك وبين عدم التحدث إطلاقًا؟ ",
" |  بين مشاهدة فيلم بمفردك أو الذهاب إلى مطعم وتناول العشاء بمفردك؟ ",
" |  بين قراءة رواية مميزة فقط أو مشاهدتها بشكل فيلم بدون القدرة على قراءتها؟ ",
" |  بين أن تكون الشخص الأكثر شعبية في العمل أو المدرسة وبين أن تكون الشخص الأكثر ذكاءً؟ ",
" |  بين إجراء المكالمات الهاتفية فقط أو إرسال الرسائل النصية فقط؟ ",
" |  بين إنهاء الحروب في العالم أو إنهاء الجوع في العالم؟ ",
" |  بين تغيير لون عينيك أو لون شعرك؟ ",
" |  بين امتلاك كل عين لون وبين امتلاك نمش على خديك؟ ",
" |  بين الخروج بالمكياج بشكل مستمر وبين الحصول على بشرة صحية ولكن لا يمكن لك تطبيق أي نوع من المكياج؟ ",
" |  بين أن تصبحي عارضة أزياء وبين ميك اب أرتيست؟ ",
" |  بين مشاهدة كرة القدم أو متابعة الأخبار؟ ",
" |  بين موت شخصية بطل الدراما التي تتابعينها أو أن يبقى ولكن يكون العمل الدرامي سيء جدًا؟ ",
" |  بين العيش في دراما قد سبق وشاهدتها ماذا تختارين بين الكوميديا والتاريخي؟ ",
" |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟ ",
" |  بين نشر تفاصيل حياتك المالية وبين نشر تفاصيل حياتك العاطفية؟ ",
" |  بين البكاء والحزن وبين اكتساب الوزن؟ ",
" |  بين تنظيف الأطباق كل يوم وبين تحضير الطعام؟ ",
" |  بين أن تتعطل سيارتك في نصف الطريق أو ألا تتمكنين من ركنها بطريقة صحيحة؟ ",
" |  بين إعادة كل الحقائب التي تملكينها أو إعادة الأحذية الجميلة الخاصة بك؟ ",
" |  بين قتل حشرة أو متابعة فيلم رعب؟ ",
" |  بين امتلاك قطة أو كلب؟ ",
" |  بين الصداقة والحب ",
" |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟ ",
" |  بين مشاركة المنزل مع عائلة من الفئران أو عائلة من الأشخاص المزعجين الفضوليين الذين يتدخلون في كل كبيرة وصغيرة؟ "]


@Client.on_message(filters.command(["لو خيروك", "خيروك"], ""))
async def bott7(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(kurok)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)